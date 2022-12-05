import pytest

from aoc8.days.d2 import Move
from aoc8.days.d2 import Result
from aoc8.days.d2 import achieve_wanted_outcome
from aoc8.days.d2 import d2_p1
from aoc8.days.d2 import d2_p2
from aoc8.days.d2 import extract_move
from aoc8.days.d2 import play


def read_data(input_path: str) -> str:
    with open(input_path, "r") as input_file:
        return input_file.read()


def test_move():
    assert Move.PAPER == extract_move("B")
    assert Move.ROCK == extract_move("X")


play_cases = [
    (Move.ROCK, Move.ROCK, Result.DRAW),
    (Move.ROCK, Move.PAPER, Result.LOSE),
    (Move.ROCK, Move.SCISSOR, Result.WIN),
    (Move.PAPER, Move.ROCK, Result.WIN),
    (Move.PAPER, Move.PAPER, Result.DRAW),
    (Move.PAPER, Move.SCISSOR, Result.LOSE),
    (Move.SCISSOR, Move.ROCK, Result.LOSE),
    (Move.SCISSOR, Move.PAPER, Result.WIN),
    (Move.SCISSOR, Move.SCISSOR, Result.DRAW),
]


@pytest.mark.parametrize("expected, opponent, wanted_outcome", play_cases)
def test_achieve_wanted_outcome(expected: Move, opponent: Move, wanted_outcome: Result) -> None:
    assert expected == achieve_wanted_outcome(opponent, wanted_outcome)


@pytest.mark.parametrize("player_move,opponent_move,result", play_cases)
def test_play(player_move: Move, opponent_move: Move, result: Result):
    actual = play(player_move, opponent_move)
    assert actual == result


test_cases_p1 = [
    ("tests/data/d2_example.txt", 15),
    ("tests/data/d2.txt", 10595),
]


@pytest.mark.parametrize("input_path, expected", test_cases_p1)
def test_d2_p1(input_path: str, expected: int) -> None:
    input_data = read_data(input_path=input_path)
    actual = d2_p1(input_data=input_data.splitlines())
    assert expected == actual


test_cases_p2 = [
    ("tests/data/d2_example.txt", 12),
    ("tests/data/d2.txt", 9541),
]


@pytest.mark.parametrize("input_path, expected", test_cases_p2)
def test_d2_p2(input_path: str, expected: int) -> None:
    input_data = read_data(input_path=input_path)
    actual = d2_p2(input_data=input_data.splitlines())
    assert expected == actual
