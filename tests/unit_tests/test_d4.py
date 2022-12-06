from aoc8.days.d4 import d4_p1
from aoc8.days.d4 import d4_p2
from aoc8.days.d4 import extract_ranges
from aoc8.days.d4 import is_fully_containing


def test_extract_ranges() -> None:
    r1, r2 = extract_ranges("2-5,6-8")
    assert r1 == {2, 3, 4, 5}
    assert r2 == {6, 7, 8}


def test_is_fully_containing():
    assert is_fully_containing({2, 3, 4}, {2, 3})


def test_d4_p1():
    assert 2 == d4_p1("tests/data/d4_example.txt")
    assert 462 == d4_p1("tests/data/d4.txt")


def test_d4_p2():
    assert 4 == d4_p2("tests/data/d4_example.txt")
    assert 835 == d4_p2("tests/data/d4.txt")
