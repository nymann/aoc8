from enum import IntEnum
from typing import Iterable, Tuple


class Move(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3


class Result(IntEnum):
    WIN = 6
    DRAW = 3
    LOSE = 0


def play(player_move: Move, opponent_move: Move) -> Result:
    if player_move == opponent_move:
        return Result.DRAW
    if player_move.value + 1 == opponent_move.value:
        return Result.LOSE
    if player_move == Move.SCISSOR and opponent_move == Move.ROCK:
        return Result.LOSE
    return Result.WIN


def extract_move(letter: str) -> Move:
    return Move(letter_to_int(letter))


def letter_to_int(letter: str) -> int:
    if ord(letter) - ord("A") > 3:
        starting_letter = "X"
    else:
        starting_letter = "A"
    return ord(letter) - ord(starting_letter) + 1


def extract_combinations(input_data: list[str]) -> Iterable[Tuple[int, int]]:
    for combination in input_data:
        opponent, player = combination.split(" ")
        yield letter_to_int(opponent), letter_to_int(player)


def extract_moves_p2(input_data: list[str]) -> Iterable[Tuple[Move, Result]]:
    r: dict[int, Result] = {1: Result.LOSE, 2: Result.DRAW, 3: Result.WIN}
    for opponent, wanted_outcome in extract_combinations(input_data=input_data):
        yield Move(opponent), r[wanted_outcome]


def extract_moves(input_data: list[str]) -> Iterable[Tuple[Move, Move]]:
    for opponent, player in extract_combinations(input_data=input_data):
        yield Move(opponent), Move(player)


def d2_p1(input_data: list[str]) -> int:
    total = 0
    for opponent_move, player_move in extract_moves(input_data):
        total += play(player_move, opponent_move).value + player_move.value

    return total


def achieve_wanted_outcome(opponent_move: Move, wanted_outcome: Result) -> Move:
    for move in [Move.ROCK, Move.PAPER, Move.SCISSOR]:
        result = play(player_move=move, opponent_move=opponent_move)
        if result == wanted_outcome:
            return move
    raise Exception("Move not found")


def d2_p2(input_data: list[str]) -> int:
    total = 0
    for opponent_move, wanted_outcome in extract_moves_p2(input_data):
        total += achieve_wanted_outcome(opponent_move, wanted_outcome).value + wanted_outcome.value

    return total
