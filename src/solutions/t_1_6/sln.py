def compress(string: str) -> str:
    if len(string) <= 2:
        return string

    chars = []
    char_count = 0

    for rp in range(0, len(string)):
        char_count += 1

        if rp == len(string) - 1 or string[rp] != string[rp + 1]:
            chars.append(string[rp])
            chars.append(str(char_count))
            char_count = 0


    return "".join(chars) if len(chars) < len(string) else string
