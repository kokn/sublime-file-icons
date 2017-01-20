import sublime

from ..common import properties


def _log(*args):
    if sublime.load_settings(properties.PACKAGE_SETTINGS_FILE).get("dev_mode"):
        text = []

        for arg in args:
            text.append(str(arg))
        print("".join(text))


def message(*args):
    _log(properties.PACKAGE_NAME, ": ", *args)


def value(*args):
    _log(properties.VALUE_PREFIX, *args)


def separator():
    _log(properties.SEPARATOR)


def done():
    _log(properties.DONE_MESSAGE)


def warning():
    print(properties.WARNING_MESSAGE)
