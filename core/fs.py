import os
import sublime

from ..common import preferences
from ..common.utils.logging import log, dump


def _is_archive():
    if os.path.splitext(preferences.PACKAGE_BASE)[1] == ".sublime-package":
        return True

    return False


def _get_packages_path():
    if _is_archive():
        return sublime.installed_packages_path()

    return sublime.packages_path()


def _get_patch_path():
    return os.path.join(sublime.packages_path(), preferences.PATCH_ROOT)


def _get_entire_path():
    pass


def _get_partial_path():
    pass


def _get_aliases_path():
    pass


def _ensure_patch():
    log("Ensure if patch exists")
    patch_path = _get_patch_path()

    if os.path.exists(patch_path):
        dump("Exists")
    else:
        log("Creating patch directory")

    if not os.path.exists(patch_path):
        os.makedirs(patch_path)


def init():
    _ensure_patch()
