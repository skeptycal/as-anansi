import sys
import unittest
from contextlib import contextmanager

from anansi import *


@contextmanager
def support(on):
    temp = antsy.SUPPORTS_COLOR
    antsy.SUPPORTS_COLOR = on
    yield
    antsy.SUPPORTS_COLOR = temp


def demo_print():
    print(f"{SUPPORTS_COLOR=}")


if __name__ == '__main__':
    demo_print()
