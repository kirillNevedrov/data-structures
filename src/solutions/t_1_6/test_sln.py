from .sln import compress

def test_compresses_string_if_compressed_string_is_shorted_than_original():
    assert compress("tttesssstt") == "t3e1s4t2"

def test_does_not_compress_string_if_compressed_string_is_equal_length_or_longer_than_original():
    assert compress("tttestt") == "tttestt"