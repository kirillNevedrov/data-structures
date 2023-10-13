from .sln import count_eval


def test_return_count_of_possible_evaluations():
    assert count_eval("1^0|0|1", False) == 2
    assert count_eval("0&0&0&1^1|0", True) == 10
