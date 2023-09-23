from typing import List


def set_to_zero(matrix: List[List[int]]) -> None:
    if len(matrix) == 0:
        return

    rows_size = len(matrix)
    columns_size = len(matrix[0])

    zero_rows = set()
    zero_columns = set()

    for row_i in range(0, rows_size):
        for col_i in range(0, columns_size):
            if matrix[row_i][col_i] == 0:
                zero_rows.add(row_i)
                zero_columns.add(col_i)

    for row_i in zero_rows:
        for col_i in range(0, columns_size):
            matrix[row_i][col_i] = 0

    for col_i in zero_columns:
        for row_i in range(0, rows_size):
            matrix[row_i][col_i] = 0
