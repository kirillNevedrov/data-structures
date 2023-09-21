from .sln import is_every_character_unique

def test_returns_true_if_every_character_is_unique():
    assert is_every_character_unique("antops") == True

def test_returns_false_if_any_character_is_not_unique():
    assert is_every_character_unique("antopts") == False