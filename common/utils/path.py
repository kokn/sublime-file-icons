import os
import sublime

from .. import preferences


def get_package_archive():
    return os.path.join(sublime.installed_packages_path(),
                        preferences.PACKAGE_BASE)


def get_package_folder():
    return os.path.join(sublime.packages_path(), preferences.PACKAGE_NAME)


def get_package_icons():
    return os.path.join(sublime.packages_path(), preferences.PACKAGE_NAME,
                        "icons")


def get_package_aliases():
    return os.path.join(sublime.packages_path(), preferences.PACKAGE_NAME,
                        "aliases")


def get_overlay():
    return os.path.join(sublime.packages_path(), preferences.OVERLAY_ROOT)


def get_overlay_aliases():
    return os.path.join(sublime.packages_path(), preferences.OVERLAY_ROOT,
                        "aliases")


def get_overlay_patches():
    return os.path.join(sublime.packages_path(), preferences.OVERLAY_ROOT,
                        "patches")


def get_overlay_patches_general():
    return os.path.join(sublime.packages_path(), preferences.OVERLAY_ROOT,
                        "patches", "general")


def get_overlay_patches_specific():
    return os.path.join(sublime.packages_path(), preferences.OVERLAY_ROOT,
                        "patches", "specific")
