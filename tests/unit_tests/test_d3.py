import pytest

from aoc8.days.d3 import Group
from aoc8.days.d3 import Item
from aoc8.days.d3 import Rucksack
from aoc8.days.d3 import d3_p1
from aoc8.days.d3 import d3_p2


def test_item() -> None:
    assert 27 == Item("A").priority()
    assert 1 == Item("a").priority()
    assert 26 == Item("z").priority()
    assert 52 == Item("Z").priority()


def test_compartments() -> None:
    rucksack = Rucksack("aA")
    assert rucksack.c1.items == ["a"]
    assert rucksack.c2.items == ["A"]


test_cases = [
    ("tests/data/d3_example.txt", 157),
    ("tests/data/d3.txt", 8233),
]


@pytest.mark.parametrize("input_path, expected", test_cases)
def test_rucksack(input_path: str, expected: int) -> None:
    assert expected == d3_p1(input_path=input_path)


test_cases_p2 = [
    ("tests/data/d3_example.txt", 70),
    ("tests/data/d3.txt", 2821),
]


@pytest.mark.parametrize("input_path, expected", test_cases_p2)
def test_rucksack_d3_p2(input_path: str, expected: int) -> None:
    assert expected == d3_p2(input_path=input_path)


def test_rucksack_duplicates():
    r = Rucksack("babA")
    assert r.duplicates() == {"b"}


def test_group():
    group = Group()
    group.add_elf(Rucksack("vJrwpWtwJgWrhcsFMMfFFhFp"))
    group.add_elf(Rucksack("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"))
    group.add_elf(Rucksack("PmmdzqPrVvPwwTWBwg"))
    assert group.duplicate_priorities() == 18


def test_group_2():
    group = Group()
    group.add_elf(Rucksack("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn"))
    group.add_elf(Rucksack("ttgJtRGJQctTZtZT"))
    group.add_elf(Rucksack("CrZsJsPPZsGzwwsLwLmpwMDw"))
    assert group.duplicate_priorities() == 52
