from aoc8.days.d5 import CrateMover9000
from aoc8.days.d5 import CrateMover9001
from aoc8.days.d5 import block_parser
from aoc8.days.d5 import index_parser
from aoc8.days.d5 import move_parser


def test_d5_p2_example():
    assert CrateMover9001("tests/data/d5_example.txt").operate() == "MCD"


def test_d5_p2():
    assert CrateMover9001("tests/data/d5.txt").operate() == "CNSFCGJSM"


def test_d5_p1_example():
    assert CrateMover9000("tests/data/d5_example.txt").operate() == "CMZ"


def test_d5_p1():
    assert CrateMover9000("tests/data/d5.txt").operate() == "RNZLFZSJH"


def test_block_parser_duplicate():
    blocks: dict[int, list[str]] = {}
    block_parser(line="[S] [S]", blocks=blocks)
    assert blocks[1][0] == "S"
    assert blocks[5][0] == "S"


def test_move_parser() -> None:
    line: str = "move 10 from 20 to 34"
    move = move_parser(line)
    assert move.amount == 10
    assert move.source == 20
    assert move.target == 34


def test_block_parser() -> None:
    blocks: dict[int, list] = {}
    block_parser("[Z] [M] [P]", blocks)
    assert [1, 5, 9] == list(blocks.keys())
    assert blocks[1] == ["Z"]
    assert blocks[5] == ["M"]
    assert blocks[9] == ["P"]


def test_index_parser() -> None:
    index_map: dict[int, int] = {}
    index_parser(line=" 1   2   3", index_map=index_map)
    assert index_map[1] == 1
    assert index_map[2] == 5
    assert index_map[3] == 9
    assert len(index_map) == 3
