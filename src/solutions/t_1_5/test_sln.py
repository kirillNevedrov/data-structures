import pytest
from .sln import is_one_edit_away


@pytest.mark.parametrize(
    "str_1, str_2",
    [
        ("test", "tes"),
        ("test", "best"),
    ],
)
def test_returns_true_if_string_one_edit_away(str_1: str, str_2: str):
    assert is_one_edit_away(str_1, str_2) == True

@pytest.mark.parametrize(
    "str_1, str_2",
    [
        ("tests", "tes"),
        ("test", "belt"),
    ],
)
def test_returns_false_if_string_more_than_one_edit_away(str_1: str, str_2: str):
    assert is_one_edit_away(str_1, str_2) == False