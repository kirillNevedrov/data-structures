class CharCount:
    char: str
    count: int

    def __init__(self, char: str, count: int) -> None:
        self.char = char
        self.count = count


def compress(string: str) -> str:
    if len(string) <= 2:
        return string

    chars_counts = [CharCount(char=string[0], count = 1)]
    for rp in range(1, len(string)):
        if string[rp] != string[rp - 1]:
            chars_counts.append(CharCount(char=string[rp], count = 1))
        else:
            chars_counts[-1].count += 1

    unique_chars_number = len(chars_counts)

    if unique_chars_number * 2 >= len(string):
        return string

    chars = []

    for c in chars_counts:
        chars.append(c.char)
        chars.append(str(c.count))

    return "".join(chars)
