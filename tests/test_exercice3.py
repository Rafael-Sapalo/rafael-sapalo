from curses.textpad import rectangle

import pytest
import sys

sys.path.append("..")

from exercice3 import *

shp = Shape()
rect = Rectangle(100, 50)
circl = Circle(100)


def test_rect_area():
    test_rect = rect.area()
    assert test_rect == 5000


def test_rect_perimeter():
    test_rect = rect.perimeter()
    assert test_rect == 300


def test_circl_area():
    test_circl = circl.area()
    assert test_circl == 31415.926535897932


def test_circl_perimeter():
    test_circl = circl.perimeter()
    assert test_circl == 628.3185307179587
