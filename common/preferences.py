import os
import sublime

from .vendor import stringcase


# GENERAL
# -----------------------------------------------------------------------------

PACKAGE_BASE = os.path.basename(os.path.dirname(os.path.dirname(__file__)))
PACKAGE_NAME = os.path.splitext(PACKAGE_BASE)[0]
PACKAGE_MAIN = stringcase.snakecase(PACKAGE_NAME.replace(" ", ""))
PACKAGE_ABBR = "".join(c for c in PACKAGE_NAME if c.isupper())

PACKAGE_SETTINGS_FILE = PACKAGE_NAME + ".sublime-settings"
SUBLIME_SETTINGS_FILE = "Preferences.sublime-settings"
PKGCTRL_SETTINGS_FILE = "Package Control.sublime-settigns"


# LOGGING
# -----------------------------------------------------------------------------

SEPARATOR = "***"

VALUE_PREFIX = " " * (len(PACKAGE_NAME) - 2) + ">>> "

RELOAD_MESSAGE = "{}\n{}: Reloading plugins\n".format(SEPARATOR,
                                                      PACKAGE_NAME)

WARNING_MESSAGE = """
{}{}: Please restart Sublime Text for the applied icons to take effect ...{}
""".format(SEPARATOR, PACKAGE_NAME, SEPARATOR)

DONE_MESSAGE = "{}: Finished".format(PACKAGE_NAME)


# HELPERS
# -----------------------------------------------------------------------------

def subltxt():
    return sublime.load_settings(SUBLIME_SETTINGS_FILE)


def pkgctrl():
    return sublime.load_settings(PKGCTRL_SETTINGS_FILE)


def package():
    return sublime.load_settings(PACKAGE_SETTINGS_FILE)
