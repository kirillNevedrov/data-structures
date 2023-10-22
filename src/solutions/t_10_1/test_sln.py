from .sln import merge


def test_merges_two_sorted_arrays_in_sorted_order():
    # arrange
    a = [1, 4, 6, 8, 10, None, None, None]
    b = [3, 7, 90]

    # act
    merge(a, 5, b, 3)

    # assert
    assert a == [1, 3, 4, 6, 7, 8, 10, 90]
