from typing import Dict

from src.queue import Queue


def count_paths_1(steps: int, memo: Dict[int, int]) -> int:
    if steps < 0:
        return 0

    if steps == 0:
        return 1

    hops = [1, 2, 3]
    sum = 0

    for hop in hops:
        new_steps = steps - hop

        if new_steps not in memo:
            memo[new_steps] = count_paths_1(new_steps, memo)

        sum += memo[new_steps]

    return sum


def count_paths_2(steps: int) -> int:
    memo: Dict[int, int] = {}

    memo[0] = 1

    hops = [1, 2, 3]

    for i in range(1, steps + 1):
        sum = 0
        for hop in hops:
            if i - hop >= 0:
                sum += memo[i - hop]

        memo[i] = sum

    return memo[steps]

def count_paths_3(steps: int) -> int:
    memo: Dict[int, int] = {}

    memo[1] = 1
    memo[2] = 0
    memo[3] = 0

    hops = [1, 2, 3]

    for _ in range(1, steps + 1):
        sum = 0
        for hop in hops:
            sum += memo[hop]

        memo[3] = memo[2]
        memo[2] = memo[1]
        memo[1] = sum

    return memo[1]
