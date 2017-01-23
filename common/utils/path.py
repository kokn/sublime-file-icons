import os
import sublime

from .. import preferences


def get_package_archive():
    return os.path.join(sublime.installed_packages_path(),
                        preferences.PACKAGE_BASE)


def get_package_folder():
    return os.path.join(sublime.packages_path(), preferences.PACKAGE_NAME)


def get_package_overlay():
    return os.path.join(sublime.packages_path(), preferences.OVERLAY_ROOT)


def get_patches():
    return os.path.join(sublime.packages_path(), preferences.OVERLAY_ROOT,
                        "patches")


def get_patches_general():
    return os.path.join(sublime.packages_path(), preferences.OVERLAY_ROOT,
                        "patches", "general")


def get_patches_specific():
    return os.path.join(sublime.packages_path(), preferences.OVERLAY_ROOT,
                        "patches", "specific")


def get_aliases():
    return os.path.join(sublime.packages_path(), preferences.OVERLAY_ROOT,
                        "aliases")
