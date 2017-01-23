import os
import shutil
import sublime
import tempfile
import zipfile

from ..common import preferences
from ..common.utils import path
from ..common.utils.logging import log, dump


def _is_enabled():
    if os.path.exists(path.get_aliases()):
        return True

    return False


def _remove_aliases():
    log("Removing aliases")

    try:
        shutil.rmtree(os.path.join(path.get_package_overlay(), "aliases"))
    except Exception as error:
        log("Error during remove")
        dump(error)


def _copy_aliases():
    log("Copying aliases")

    package_path = path.get_package_folder()
    overlay_path = path.get_package_overlay()

    src = os.path.join(package_path, "aliases")
    dest = os.path.join(overlay_path, "aliases")

    try:
        shutil.copytree(src, dest)
    except Exception as error:
        log("Error during copy")
        dump(error)


def _extract_aliases():
    log("Extracting aliases")

    temp_dir = tempfile.mkdtemp()
    dest_path = path.get_aliases()

    try:
        with zipfile.ZipFile(path.get_package_archive(), "r") as z:
            members = z.namelist()
            members_to_extract = [
                m for m in members if m.startswith("aliases")
            ]

            z.extractall(temp_dir, members_to_extract)

            for file in os.listdir(temp_dir):
                print(file)

            shutil.move(os.path.join(temp_dir, "aliases"), dest_path)
    except Exception as error:
        log("Error during extract")
        dump(error)


def enable():
    if preferences.is_package_archive():
        _extract_aliases()
    else:
        _copy_aliases()


def disable():
    _remove_aliases()


def init():
    log("Initializing aliases")

    if preferences.package().get("aliases"):
        if not _is_enabled():
            enable()
        else:
            dump("All the necessary alias files are provided")
    else:
        if _is_enabled():
            disable()
