from collections.abc import Iterable
from typing import Self

from aoc8.util import read_data


class Item:
    def __init__(self, item: str) -> None:
        self.item = item

    def priority(self) -> int:
        if self.item.islower():
            return ord(self.item) - ord("a") + 1
        return ord(self.item) - ord("A") + 27


class Compartment:
    def __init__(self, items: str) -> None:
        self.items = [item for item in items]

    def distinct(self) -> set[str]:
        return set(self.items)

    def duplicates(self, other: Self) -> Iterable[Item]:
        a = self.distinct()
        b = other.distinct()
        dupes = a - (a ^ b)
        for item in dupes:
            yield Item(item)


class Rucksack:
    def __init__(self, items: str) -> None:
        half_idx = len(items) // 2
        self.c1 = Compartment(items=items[:half_idx])
        self.c2 = Compartment(items=items[half_idx:])
        self.items: set[str] = set(item for item in items)

    def duplicate_priorities(self) -> int:
        total = 0
        for item in self.c1.duplicates(self.c2):
            total += item.priority()
        return total

    def duplicates(self) -> set[str]:
        return {item.item for item in self.c1.duplicates(self.c2)}


class Group:
    def __init__(self) -> None:
        self.rucksacks: list[Rucksack] = []

    def add_elf(self, rucksack: Rucksack) -> None:
        self.rucksacks.append(rucksack)

    def duplicates(self) -> Iterable[Item]:
        a = self.rucksacks[0].items
        b = self.rucksacks[1].items
        c = self.rucksacks[2].items
        dupes = c - (c ^ (a - (a ^ b)))
        for dupe in dupes:
            yield Item(dupe)

    def duplicate_priorities(self) -> int:
        return sum(item.priority() for item in self.duplicates())


def d3_p1(input_path: str) -> int:
    total = 0
    for line in read_data(input_path).splitlines():
        total += Rucksack(items=line).duplicate_priorities()
    return total


def d3_p2(input_path: str) -> int:
    total = 0
    group = Group()
    for line in read_data(input_path).splitlines():
        rucksack = Rucksack(line)
        group.add_elf(rucksack)
        if len(group.rucksacks) == 3:
            total += group.duplicate_priorities()
            group = Group()
    return total
