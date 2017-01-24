import os
import shutil
import sublime
import tempfile
import zipfile

from ..common import preferences
from ..common.utils import path
from ..common.utils.logging import log, dump


def _is_enabled():
    if os.path.exists(path.get_overlay_aliases()):
        return True

    return False


def _remove():
    log("Removing aliases")

    try:
        shutil.rmtree(path.get_overlay_aliases())
    except Exception as error:
        log("Error during remove")
        dump(error)


def _rename():
    log("Renaming aliases")

    aliases_path = path.get_overlay_aliases()

    try:
        for alias_base in os.listdir(aliases_path):
            alias_path = os.path.join(aliases_path, alias_base)

            if os.path.isfile(alias_path):
                name, ext = os.path.splitext(alias_path)
                os.rename(alias_path, alias_path.replace(".disabled-", "."))
    except Exception as error:
        log("Error during rename")
        dump(error)


def _copy():
    log("Copying aliases")

    src = path.get_package_aliases()
    dest = path.get_overlay_aliases()

    try:
        shutil.copytree(src, dest)
    except Exception as error:
        log("Error during copy")
        dump(error)
    else:
        _rename()


def _extract():
    log("Extracting aliases")

    temp_dir = tempfile.mkdtemp()
    dest_path = path.get_overlay_aliases()

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
    else:
        _rename()


def enable():
    if not _is_enabled():
        if preferences.is_package_archive():
            sublime.set_timeout_async(_extract, 0)
        else:
            sublime.set_timeout_async(_copy, 0)
    else:
        dump("Aliases already enabled")


def disable():
    if _is_enabled():
        sublime.set_timeout_async(_remove, 0)
    else:
        dump("Aliases already disabled")


def check():
    log("Checking aliases")

    if preferences.package().get("aliases"):
        enable()
    else:
        disable()
