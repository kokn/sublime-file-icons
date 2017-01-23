import functools

from .. import preferences


def _tags():
    if preferences.package().get("dev_mode"):
        return preferences.package().get("dev_trace", [])
    else:
        return []


def _trace(*args, tag="standard", **kwargs):
    if tag not in _tags():
        return

    text = []

    for arg in args:
        text.append(str(arg))

    print("".join(text), **kwargs)


def log(*args, **kwargs):
    _trace(preferences.PACKAGE_NAME, ": ", *args, **kwargs)


def dump(*args, **kwargs):
    _trace(preferences.PREFIX, *args, **kwargs)


def done():
    _trace(preferences.DONE_MESSAGE)


def warning():
    _trace(preferences.WARNING_MESSAGE)


def log_tag(tag):
    return functools.partial(log, tag=tag)


def dump_tag(tag):
    return functools.partial(dump, tag=tag)


log.tag = log_tag
dump.tag = dump_tag
