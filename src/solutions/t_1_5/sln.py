from typing import Dict, List


def is_one_edit_away(str_1: str, str_2: str) -> bool:
    if abs(len(str_1) - len(str_2)) > 1:
        return False

    chars_counts = {}

    for c in str_1:
        if c in chars_counts:
            chars_counts[c] += 1
        else:
            chars_counts[c] = 1

    for c in str_2:
        if c in chars_counts:
            chars_counts[c] -= 1
        else:
            chars_counts[c] = -1

    str_1_counts = 0
    str_2_counts = 0

    for c in chars_counts.values():
        if c > 0:
            str_1_counts += c
        elif c < 0:
            str_2_counts += -c

    if str_1_counts > 0 and str_2_counts > 0:
        str_1_counts -= 1
        str_2_counts -= 1

    return str_1_counts + str_2_counts <= 1
