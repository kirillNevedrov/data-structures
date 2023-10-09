# def insert_number(n: int, m: int, i: int, j: int) -> int:
#     for bit_index in range(0, j - i + 1):
#         m_bit = get_bit(number=m, index=bit_index)

#         if m_bit:
#             n = set_bit(number=n, index=i + bit_index)
#         else:
#             n = clear_bit(number=n, index=i + bit_index)

#     return n


# def get_bit(number: int, index: int) -> bool:
#     return (number & (1 << index)) != 0


# def set_bit(number: int, index: int) -> int:
#     return number | (1 << index)


# def clear_bit(number: int, index: int) -> int:
#     mask = ~(1 << index)
#     return number & mask


def insert_number(n: int, m: int, i: int, j: int) -> int:
    all_ones = ~0

    left = all_ones << (j + 1) if j < 31 else 0
    right = (i << 1) - 1
    mask = left | right

    n_cleared = n & mask
    m_shifted = m << i

    return n_cleared | m_shifted
