from .sln import rotate


def test_rotates_matrix():
    # arrange
    matrix = [
        [1, 2, 3],
        [17, 5, 91],
        [0, 0, 1000],
    ]

    # act
    rotate(matrix)

    # assert
    assert matrix == [
        [3, 91, 1000],
        [2, 5, 0],
        [1, 17, 0],
    ]
