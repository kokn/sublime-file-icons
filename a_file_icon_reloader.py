"""
A File Icon Reloader

Based on https://github.com/math2001/sublime-plugin-reloader.

All credit goes to Mathieu Paturel <@math2001>
"""

import imp
import os
import sublime
import sublime_plugin
import sys
import traceback

from .common import properties
from .common import settings


class AfiReloadListener(sublime_plugin.EventListener):
    def on_post_save(self, view):
        if not (os.path.dirname(__file__) in view.file_name() and
                view.file_name().endswith(".py")):
            return

        sublime.run_command("afi_reload", {
            "main": os.path.join(sublime.packages_path(),
                                 properties.PACKAGE_NAME,
                                 properties.PACKAGE_MAIN),
            "folders": [
                "vendor",
                "templates",
                "common",
                "utils",
                "core"
            ],
            "times": 1,
            "quiet": not settings.package().get("dev_mode", False)
        })


class AfiReloadCommand(sublime_plugin.ApplicationCommand):
    def reload(self, main, scripts, folders, times):
        if int(sublime.version()) > 3:
            main = sublime.expand_variables(main, sublime.active_window()
                                                         .extract_variables())
        base_path = os.path.dirname(main)
        pck_name = os.path.basename(base_path)

        for folder in folders:
            sys.path.append(os.path.join(base_path, folder))

            for item in os.listdir(os.path.join(base_path, folder)):
                root, ext = os.path.splitext(item)

                if (os.path.isfile(os.path.join(base_path, folder, item)) and
                        ext == ".py" and root != "__init__"):
                    module = ".".join(
                        [pck_name, folder, os.path.splitext(item)[0]])

                    print(properties.VALUE_PREFIX, end="")
                    sublime_plugin.reload_plugin(module)
            sys.path.pop()

        for script in scripts:
            module = pck_name + "." + (script[:-3]
                                       if script.endswith(".py") else script)

            print(properties.VALUE_PREFIX, end="")
            sublime_plugin.reload_plugin(module)

        module = sys.modules[pck_name + "." + os.path.splitext(
            os.path.basename(main))[0]]

        print(properties.VALUE_PREFIX, end="")
        sublime_plugin.reload_plugin(module.__name__)

        if times > 1:
            return self.reload(main, scripts, folders, times - 1)

    def run(self, main, scripts=[], folders=[], times=2, quiet=True):
        sys.stdout.write(properties.RELOAD_MESSAGE)
        sys.stdout.flush()

        if quiet:
            stdout_write = sys.stdout.write
            sys.stdout.write = lambda text: "do nothing"

        try:
            self.reload(main, scripts, folders, times)
        except:
            traceback.print_exc()

        if quiet:
            sys.stdout.write = stdout_write
