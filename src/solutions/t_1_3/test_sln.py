from .sln import utlify


def test_replaces_spaces_by_unicode_encoding():
    assert (
        utlify("Hi, this is the string        ", 22) == "Hi,%20this%20is%20the%20string"
    )
