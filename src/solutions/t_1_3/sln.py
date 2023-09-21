def utlify(string: str, length: int) -> str:
    chars = [c for c in string]
    offset = 0

    for i in range(0, length):
        if chars[i] == " ":
            offset += 2

    wp = length - 1 + offset
    for rp in range(length - 1, -1, -1):
        if chars[rp] != " ":
            chars[wp] = chars[rp]
            wp -= 1
        else:
            chars[wp - 2] = "%"
            chars[wp - 1] = "2"
            chars[wp] = "0"

            wp -= 3

            if wp <= rp:
                break

    return "".join(chars)
