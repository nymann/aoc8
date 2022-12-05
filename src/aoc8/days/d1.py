from typing import Iterable


class Elf:
    def __init__(self) -> None:
        self.calories = 0

    def add_calories(self, calories: int) -> None:
        self.calories += calories


def elfs(input_data: str) -> Iterable[Elf]:
    for elf_input in input_data.split("\n\n"):
        elf = Elf()
        for food in elf_input.splitlines():
            elf.add_calories(int(food))
        yield elf


def d1_p1(input_data: str) -> int:
    return max(elf.calories for elf in elfs(input_data))


def d1_p2(input_data: str) -> int:
    elf_calories: list[int] = [elf.calories for elf in elfs(input_data)]
    elf_calories.sort(reverse=True)
    return sum(elf_calories[:3])
