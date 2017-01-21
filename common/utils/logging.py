from .. import preferences


def _log(*args, **kwargs):
    text = []

    for arg in args:
        text.append(str(arg))

    print("".join(text), **kwargs)


def msg(*args, **kwargs):
    _log(preferences.PACKAGE_NAME, ": ", *args, **kwargs)


def val(*args, **kwargs):
    _log(preferences.VALUE_PREFIX, *args, **kwargs)


def sep():
    _log(preferences.SEPARATOR)
