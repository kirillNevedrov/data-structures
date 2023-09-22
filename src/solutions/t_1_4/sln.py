def is_palindrome_permutation(string: str) -> bool:
    characters_counts = {}
    length = 0

    for c in string:
        if c == " ":
            continue

        c = c.lower()

        if c in characters_counts:
            characters_counts[c] += 1
        else:
            characters_counts[c] = 1

        length += 1

    if length == 0:
        return False

    if length % 2 == 0:
        for c in characters_counts.values():
            if c % 2 != 0:
                return False
    else:
        odd_counts_count = 0
        for c in characters_counts.values():
            if c % 2 != 0:
                odd_counts_count += 1

                if odd_counts_count > 1:
                    return False

    return True


# def is_palindrome(string: str) -> bool:
#     string = string.lower().replace(" ", "")

#     if len(string) < 2:
#         return False

#     lp = len(string) // 2 - 1
#     rp = (len(string) + 1) // 2

#     while lp >= 0:
#         if string[lp] != string[rp]:
#             return False

#         lp -= 1
#         rp += 1

#     return True
