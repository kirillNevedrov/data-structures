from typing import List


def get_permutations(string: List[str]) -> List[List[str]]:
    if len(string) == 0:
        return []

    if len(string) == 1:
        return [string]

    permutations = get_permutations(string[1:])

    new_permutations = []
    for p in permutations:
        for i in range(0, len(p) + 1):
            new_permutations.append(insert_char(p, string[0], i))

    return new_permutations


def insert_char(string: List[str], char: str, index: int) -> List[str]:
    return string[:index] + [char] + string[index:]
