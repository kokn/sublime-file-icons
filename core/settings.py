import sublime
import json

from ..common import preferences
from ..common.vendor import jsonutils
from ..common.utils.logging import log, dump

PACKAGE_DEFAULT_SETTINGS = {}
PACKAGE_CURRENT_SETTINGS = {}


def _get_default_settings():
    return json.loads(jsonutils.sanitize_json(sublime.load_resource(
        "Packages/{0}/.sublime/{0}.sublime-settings"
        .format(preferences.PACKAGE_NAME)
    )))


def init():
    log("Initializing settings")

    global PACKAGE_DEFAULT_SETTINGS

    PACKAGE_DEFAULT_SETTINGS = _get_default_settings()

    update()


def update():
    log("Updating the current settings")

    global PACKAGE_CURRENT_SETTINGS

    for s in PACKAGE_DEFAULT_SETTINGS:
        PACKAGE_CURRENT_SETTINGS[s] = preferences.package().get(s)

    dump(PACKAGE_CURRENT_SETTINGS)
