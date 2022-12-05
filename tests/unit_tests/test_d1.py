from pydantic import BaseModel
import pytest

from aoc8.days.d1 import d1_p1
from aoc8.days.d1 import d1_p2


class TestCase(BaseModel):
    __test__ = False
    input_data: str

    @classmethod
    def from_file(cls, input_path: str) -> "TestCase":
        with open(input_path, "r") as input_file:
            return cls(input_data=input_file.read())


t1 = TestCase(input_data="1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000")
t2 = TestCase.from_file("tests/data/d1.txt")

test_cases_p1 = [
    (t1, 24000),
    (t2, 70698),
]
test_cases_p2 = [
    (t1, 45000),
    (t2, 206643),
]


@pytest.mark.parametrize("test_case, expected", test_cases_p1)
def test_d1_p1(test_case: TestCase, expected: int) -> None:
    actual = d1_p1(input_data=test_case.input_data)
    assert expected == actual


@pytest.mark.parametrize("test_case, expected", test_cases_p2)
def test_d1_p2(test_case: TestCase, expected: int) -> None:
    actual = d1_p2(input_data=test_case.input_data)
    assert expected == actual
