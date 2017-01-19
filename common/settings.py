import sublime
import os
import json

from ..vendor import stringcase
from ..vendor import jsonutils


# COMMON
# -----------------------------------------------------------------------------

def get_package_name():
    name = os.path.basename(os.path.dirname(os.path.dirname(__file__)))

    if name.endswith(".sublime-package"):
        name = name[:-16]

    return name


PACKAGE_NAME = get_package_name()
PACKAGE_MAIN = stringcase.snakecase(PACKAGE_NAME.replace(" ", "")) + ".py"

PACKAGE_SETTINGS_FILE = PACKAGE_NAME + ".sublime-settings"
SUBLIME_SETTINGS_FILE = "Preferences.sublime-settings"
PKGCTRL_SETTINGS_FILE = "Package Control.sublime-settigns"


# MESSAGES
# -----------------------------------------------------------------------------

WARNING_MESSAGE = """
Please restart Sublime Text for the applied icons to take effect ...
"""


# LOGGING
# -----------------------------------------------------------------------------

TOP_SEPARATOR = "\n***"
BOTTOM_SEPARATOR = "***\n"

VALUE_PREFIX = "        >>> "


# HELPERS
# -----------------------------------------------------------------------------

def subltxt():
    return sublime.load_settings(SUBLIME_SETTINGS_FILE)


def pkgctrl():
    return sublime.load_settings(PKGCTRL_SETTINGS_FILE)


def package():
    return sublime.load_settings(PACKAGE_SETTINGS_FILE)
