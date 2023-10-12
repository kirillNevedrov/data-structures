from .sln import get_permutations


def test_returns_string_permutations():
    # arrange
    string = ["c", "a", "t"]

    # act
    permutations = get_permutations(string)

    # assert
    permutation_strings = ["".join(p) for p in permutations]
    assert len(permutation_strings) == 6
    assert all(
        s in permutation_strings for s in ["cat", "cta", "act", "atc", "tca", "tac"]
    )
