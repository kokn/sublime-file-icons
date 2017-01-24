import os
import re
import sublime
import sublime_plugin

from ..common import preferences
from ..common.utils import path
from ..common.utils.logging import log, dump

from . import settings

THEME_PATTERN = re.compile(r"^Packages/|\/.*$")
COLOR_PATTERN = re.compile(r"#([A-Fa-f0-9]{6})")


def _get_colors():
    colors = {}
    package_settings = preferences.package()
    color_options = [
        o for o in settings.PACKAGE_DEFAULT_SETTINGS if o.startswith("color")
    ]

    if package_settings.get("color"):
        for opt in color_options:
            color = package_settings.get(opt)

            if re.match(COLOR_PATTERN, color):
                hex_color = color.lstrip("#")
                rgb_color = [
                    int(hex_color[i: i + 2], 16) for i in (0, 2, 4)
                ]

                color = ", ".join(str(e) for e in rgb_color)

                colors[opt] = ("[" + color + "]")
            else:
                colors.append("")
    return colors


def _get_settings():
    log("Getting theme settings")
    ts = {}
    ts["colors"] = _get_colors()
    ts["opacity"] = preferences.package().get("opacity")
    ts["opacity_on_hover"] = preferences.package().get("opacity_on_hover")
    ts["opacity_on_select"] = preferences.package().get("opacity_on_select")
    ts["size"] = preferences.package().get("size")

    dump(ts)
    return ts


def _patch_general(themes, theme_settings):
    dest = os.path.join(path.get_overlay_patches_general(), "multi")

    if theme_settings["colors"]:
        dest = os.path.join(path.get_overlay_patches_general(), "single")

    print(dest)


def _patch_specific(themes, colors):
    pass


def get_current():
    log("Getting the current theme")

    current = preferences.subltxt().get("theme")
    dump(current)

    return current


def get_installed():
    log("Getting installed themes")

    theme_resources = sublime.find_resources("*.sublime-theme")
    installed_themes = {}

    for res in theme_resources:
        package = re.sub(THEME_PATTERN, "", res)
        theme = os.path.basename(res)

        installed_themes.setdefault(package, []).append(theme)

    if preferences.OVERLAY_ROOT in installed_themes:
        del installed_themes[preferences.OVERLAY_ROOT]

    dump(installed_themes)

    return installed_themes


def get_customizable():
    log("Getting the list of theme packages with customization support")

    customizable_themes = []

    prev_res = sublime.find_resources(".st-file-icons")
    curr_res = sublime.find_resources(".supports-a-file-icon-customization")

    theme_res = prev_res + curr_res

    for res in theme_res:
        customizable_themes.append(re.sub(THEME_PATTERN, "", res))

    dump(customizable_themes)

    return customizable_themes


class AfiPatchCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        log("Patching themes")
        installed_themes = get_installed()
        customizable_themes = get_customizable()
        theme_settings = _get_settings()

        for theme in installed_themes:
            _patch_general(installed_themes[theme], theme_settings)

