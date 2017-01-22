import os

from ..common import properties


def _is_archive():
    if os.path.splitext(properties.PACKAGE_BASE)[1] == ".sublime-package":
        return True

    return False


def _check_patch_dir():
    pass


def init():
    pass
