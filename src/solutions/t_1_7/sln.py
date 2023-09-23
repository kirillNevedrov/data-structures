from typing import List


def rotate(matrix: List[List[int]]) -> None:
    size = len(matrix)
    for row_i in range(0, size):
        for column_i in range(row_i, size - 1 - row_i):
            current_row_i = row_i
            current_column_i = column_i
            current_temp = matrix[row_i][column_i]
            for _ in range(0, 4):
                new_row_i = size - 1 - current_column_i
                new_column_i = current_row_i
                new_temp = matrix[new_row_i][new_column_i]

                matrix[new_row_i][new_column_i] = current_temp
                current_row_i = new_row_i
                current_column_i = new_column_i
                current_temp = new_temp
