from ..common import settings


def log(*args):
    text = []

    for arg in args:
        text.append(str(arg))
    print("".join(text))
