from typing import Tuple

from aoc8.util import read_data


def extract_ranges(line: str) -> Tuple[set[int], set[int]]:
    elf1, elf2 = line.split(",")
    return sections(elf1), sections(elf2)


def sections(from_to_dashed: str) -> set[int]:
    a, b = from_to_dashed.split("-")
    start = int(a)
    stop = int(b)
    return set({i for i in range(start, stop + 1)})


def is_fully_containing(r1: set[int], r2: set[int]) -> bool:
    r1_contains_r2 = not bool(r1 - r2)
    r2_contains_rl = not bool(r2 - r1)

    return r1_contains_r2 or r2_contains_rl


def is_partially_containing(r1: set[int], r2: set[int]) -> bool:
    r1_contains_r2 = len(r1) > len(r1 - r2)
    r2_contains_rl = len(r2) > len(r2 - r1)

    return r1_contains_r2 or r2_contains_rl


def d4_p1(input_path: str) -> int:
    total = 0
    for line in read_data(input_path).splitlines():
        r1, r2 = extract_ranges(line=line)
        if is_fully_containing(r1, r2):
            total += 1

    return total


def d4_p2(input_path: str) -> int:
    total = 0
    for line in read_data(input_path).splitlines():
        r1, r2 = extract_ranges(line=line)
        if is_partially_containing(r1, r2):
            total += 1

    return total
