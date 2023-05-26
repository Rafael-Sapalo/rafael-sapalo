import pytest
import sys

sys.path.append("..")

from exercice2 import StringAnalyzer

proc = StringAnalyzer("python")


def test_count_wowels():
    test = proc.count_vowels()
    assert test == 1


def test_count_consonants():
    test = proc.count_consonants()
    assert test == 5


def test_count_digits():
    test = proc.count_digits()
    assert test == 0


def test_count_words():
    test = proc.count_words()
    assert test == 1


def test_count_lines():
    test = proc.count_lines()
    assert test == 1
