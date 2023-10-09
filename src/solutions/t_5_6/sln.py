def get_number_of_flips(n: int, m: int) -> int:
    diff = n ^ m

    flips = 0

    while diff != 0:
        flips += diff & 1

        diff >>= 1

    return flips


def get_bit(number: int, index: int) -> bool:
    return (number & (1 << index)) != 0
