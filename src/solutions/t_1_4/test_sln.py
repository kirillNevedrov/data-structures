from .sln import is_palindrome_permutation


def test_returns_true_if_string_is_palindrome_permutation():
    assert is_palindrome_permutation("Tact Coa") == True


def test_returns_false_if_string_is_not_palindrome_permutation():
    assert is_palindrome_permutation("Tack Coa") == False


# def test_returns_true_if_string_is_palindrome():
#     assert is_palindrome("Taco Cat") == True


# def test_returns_false_if_string_is_not_palindrome():
#     assert is_palindrome("Tact Coa") == False
