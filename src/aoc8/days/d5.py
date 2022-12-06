from collections.abc import Iterable
import re

from pydantic import BaseModel

from aoc8.util import read_data


class Move(BaseModel):
    amount: int
    source: int
    target: int


class CrateMover9000:
    def __init__(self, input_path: str) -> None:
        self.blocks: dict[int, list[str]] = {}
        self.index_map: dict[int, int] = {}
        self._input_path = input_path

    def operate(self) -> str:
        for move in self._parse():
            self._do_move(move)
        return self._get_top()

    def _do_move(self, move: Move) -> None:
        source_idx = self.index_map[move.source]
        target_idx = self.index_map[move.target]
        for _ in range(move.amount):
            block = self.blocks[source_idx].pop(0)
            self.blocks[target_idx].insert(0, block)

    def _parse(self) -> Iterable[Move]:
        for line in read_data(self._input_path).splitlines():
            if "[" in line:
                block_parser(line=line, blocks=self.blocks)
            elif "move" in line:
                yield move_parser(line=line)
            elif line.strip():
                index_parser(line=line, index_map=self.index_map)

    def _get_top(self) -> str:
        on_top: list[str] = []
        for index in self.index_map.values():
            stack = self.blocks[index]
            if stack:
                on_top.append(stack[0])

        return "".join(on_top)


class CrateMover9001(CrateMover9000):
    def _do_move(self, move: Move) -> None:
        source_idx = self.index_map[move.source]
        target_idx = self.index_map[move.target]
        for i in range(move.amount, 0, -1):
            block = self.blocks[source_idx].pop(i - 1)
            self.blocks[target_idx].insert(0, block)


def index_parser(line: str, index_map: dict[int, int]) -> None:
    for number in re.findall(r"\d+", line):
        index_map[int(number)] = line.index(number)


def move_parser(line: str) -> Move:
    amount, source, target = re.findall(r"\d+", line)
    return Move(amount=amount, source=source, target=target)


def block_parser(line: str, blocks: dict[int, list[str]]) -> None:
    for match in re.finditer("[A-Z]", line):
        idx = match.start()
        if idx not in blocks:
            blocks[idx] = []
        blocks[idx].append(line[idx])
