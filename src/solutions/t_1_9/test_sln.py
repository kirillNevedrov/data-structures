from .sln import is_rotation


def test_returns_true_if_one_string_is_rotation_of_other():
    assert is_rotation("waterbottle", "erbottlewat") == True


def test_returns_false_if_one_string_is_not_rotation_of_other():
    assert is_rotation("waterbottle", "erbottlewta") == False
