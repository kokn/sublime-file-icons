import json
import os
import sublime
import sublime_plugin
import textwrap

from ..common import properties
from ..common import settings


def _get_package_version():
    pkg_json = sublime.load_resource("Packages/" + properties.PACKAGE_NAME +
                                     "/package.json")

    return json.loads(pkg_json)["version"]


def _is_installed_via_pc():
    return str(properties.PACKAGE_NAME in set(settings.pkgctrl()
                                              .get("installed_packages", [])))


def _get_current_theme():
    return settings.subltxt().get("theme")


def _get_installed_themes():
    installed_resources = sublime.find_resources("*.sublime-theme")
    installed_themes = {}

    for res in installed_resources:
        installed_themes.setdefault(os.path.basename(os.path.dirname(res)),
                                    []).append(os.path.basename(res))

    # if "z file icon" in installed_themes:
    #     del installed_themes["z file icon"]

    return installed_themes


class AfiEnvironmentCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        info = {}

        info["platform"] = sublime.platform()
        info["sublime_version"] = sublime.version()

        info["package_version"] = _get_package_version()
        info["installed_via_pc"] = _is_installed_via_pc()
        info["current_theme"] = _get_current_theme()
        info["installed_themes"] = _get_installed_themes()

        msg = textwrap.dedent(
            """\
            - A File Icon: %(package_version)s
            - Sublime Text: %(sublime_version)s
            - Platform: %(platform)s
            - Package Control: %(installed_via_pc)s
            - Current Theme: %(current_theme)s
            - Installed Themes: %(installed_themes)s
            """ % info
        )

        view = sublime.active_window().active_view()

        def copy_and_hide(msg):
            sublime.set_clipboard(msg)
            view.hide_popup()

        view.show_popup(msg.replace("\n", "<br>") +
                        "<br><a href=\"" + msg + "\">Copy</a>",
                        on_navigate=copy_and_hide)
