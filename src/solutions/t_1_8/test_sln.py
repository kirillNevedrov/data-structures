from .sln import set_to_zero


def test_set_colums_and_rows_with_zero_to_zero():
    # arrange
    matrix = [
        [1, 2, 3],
        [17, 5, 91],
        [0, 0, 1000],
    ]

    # act
    set_to_zero(matrix)

    # assert
    assert matrix == [
        [0, 0, 3],
        [0, 0, 91],
        [0, 0, 0],
    ]
