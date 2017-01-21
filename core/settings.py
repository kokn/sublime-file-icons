import sublime
import json

from . import properties
from ..utils import logging
from ..vendor import jsonutils

PACKAGE_DEFAULT_SETTINGS = {}
PACKAGE_CURRENT_SETTINGS = {}


def _get_default_settings():
    return json.loads(jsonutils.sanitize_json(sublime.load_resource(
        "Packages/{0}/.sublime/{0}.sublime-settings"
        .format(properties.PACKAGE_NAME)
    )))


def init():
    logging.message("Initializing settings")

    global PACKAGE_DEFAULT_SETTINGS

    PACKAGE_DEFAULT_SETTINGS = _get_default_settings()

    update()


def update():
    logging.message("Updating the current settings")

    global PACKAGE_CURRENT_SETTINGS

    for s in PACKAGE_DEFAULT_SETTINGS:
        PACKAGE_CURRENT_SETTINGS[s] = package().get(s)

    logging.value(PACKAGE_CURRENT_SETTINGS)
