from .sln import count_paths_1, count_paths_2, count_paths_3


def test_1_returns_number_of_possible_paths():
    assert count_paths_1(3, {}) == 4


def test_2_returns_number_of_possible_paths():
    assert count_paths_2(3) == 4


def test_3_returns_number_of_possible_paths():
    assert count_paths_3(3) == 4
