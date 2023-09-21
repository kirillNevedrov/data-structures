from .sln import is_permutation

def test_returns_true_if_one_string_is_permutation_of_other():
    assert is_permutation("antopts", "tnaospt") == True

def test_returns_false_if_one_string_is_not_permutation_of_other():
    assert is_permutation("antopts", "tnaispt") == False