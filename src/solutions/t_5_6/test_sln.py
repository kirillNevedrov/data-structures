from .sln import get_number_of_flips


def test_returns_number_of_flips():
    assert get_number_of_flips(0b11101, 0b01111) == 2
