import os
import shutil
import sublime
import tempfile
import zipfile

from ..common import preferences
from ..common.utils import path
from ..common.utils.logging import log, dump


def _create_dirs():
    log("Creating directories")

    try:
        g = path.get_patches_general()
        s = path.get_patches_specific()

        if not os.path.exists(g):
            os.makedirs(g)

            if not os.path.exists(s):
                os.makedirs(s)
    except Exception as error:
        log("Error during create")
        dump(error)


def _extract_general():
    log("Extracting general icons")

    temp_dir = tempfile.mkdtemp()
    dest_path = path.get_patches_general()

    try:
        with zipfile.ZipFile(path.get_package_archive(), "r") as z:
            members = z.namelist()
            members_to_extract = [m for m in members if m.startswith("icons")]

            z.extractall(temp_dir, members_to_extract)

            shutil.move(os.path.join(temp_dir, "icons", "single"), dest_path)
            shutil.move(os.path.join(temp_dir, "icons", "multi"), dest_path)
    except Exception as error:
        log("Error during extract")
        dump(error)


def _copy_general():
    log("Copying general icons")

    package_path = path.get_package_folder()
    general_path = path.get_patches_general()

    src_multi = os.path.join(package_path, "icons", "multi")
    src_single = os.path.join(package_path, "icons", "single")

    dest_multi = os.path.join(general_path, "multi")
    dest_single = os.path.join(general_path, "single")

    try:
        shutil.copytree(src_multi, dest_multi)
        shutil.copytree(src_single, dest_single)
    except Exception as error:
        log("Error during copy")
        dump(error)


def provide():
    if preferences.is_package_archive():
        _extract_general()
    else:
        _copy_general()


def init():
    log("Checking icons")

    if os.path.exists(path.get_package_overlay()):
        dump("All the necessary icon files are provided")
    else:
        _create_dirs()
        sublime.set_timeout_async(provide, 0)
