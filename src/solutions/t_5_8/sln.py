def draw_line(screen: bytearray, width: int, x_1: int, x_2: int, y: int) -> None:
    start_index = y * 32 + x_1
    end_index = y * 32 + x_2

    index = start_index

    while index <= end_index:
        byte_index = get_byte_index(index)

        left_one_index = 7 - (index - (byte_index * 8))
        right_one_index = 7 - min(7, end_index - (byte_index * 8))

        left = (1 << left_one_index + 1) - 1
        right = -1 << right_one_index
        mask = left & right & 255

        byte = screen[byte_index]
        screen[byte_index] = byte | mask

        index = (byte_index + 1) * 8


def get_byte_index(index: int) -> int:
    return index // 8
