import os
import re
import sublime

from ..common import preferences
from ..common.utils.logging import log, dump

PATTERN = re.compile(r"^Packages/|\/.*$")
INSTALLED_THEMES = {}
CUSTOMIZABLE_THEMES = {}


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
        package = re.sub(PATTERN, "", res)
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
        customizable_themes.append(re.sub(PATTERN, "", res))

    dump(customizable_themes)

    return customizable_themes
