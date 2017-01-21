import functools

from . import logging
from .. import preferences


def get_tags():
    if preferences.package().get("dev_mode"):
        return preferences.package().get("dev_trace", [])
    else:
        return []


def trace(*args, tag="debug", type="msg", fill=None, fill_width=60, **kwargs):
    """
    Lightweight logging facility. Provides simple print-like interface with
    filtering by tags and pretty-printed captions for delimiting output
    sections.

    See the "dev_trace" setting for possible values of the "tag" keyword.
    """
    if tag not in get_tags():
        return

    if fill is not None:
        sep = str(kwargs.get("sep", " "))
        caption = sep.join(args)
        args = "{0:{fill}<{width}}".format(caption and caption + sep,
                                           fill=fill, width=fill_width),

    return {
        "msg": logging.msg(preferences.PACKAGE_ABBR + " [{}]".format(tag),
                           *args, **kwargs),
        "sep": logging.sep()
    }[type]


    print()


def trace_for_tag(tag):
    return functools.partial(trace, tag=tag)


trace.for_tag = trace_for_tag


class StackMeter:
    """
    Reentrant context manager counting the reentrancy depth.
    """

    def __init__(self, depth=0):
        super().__init__()
        self.depth = depth

    def __enter__(self):
        depth = self.depth
        self.depth += 1
        return depth

    def __exit__(self, *exc_info):
        self.depth -= 1
