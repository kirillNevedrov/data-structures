from typing import Dict


def is_permutation(string_1: str, string_2: str) -> bool:
    if len(string_1) != len(string_2):
        return False

    counters_1 = string_to_characters_counters(string_1)
    counters_2 = string_to_characters_counters(string_2)

    for k, v in counters_1.items():
        if v != counters_2.get(k):
            return False

    return True


def string_to_characters_counters(string: str) -> Dict[str, int]:
    counters = {}
    for c in string:
        if c in counters:
            counters[c] += 1
        else:
            counters[c] = 1

    return counters
