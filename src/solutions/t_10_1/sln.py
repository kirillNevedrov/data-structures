from typing import List


def merge(a: List[int], a_len: int, b: List[int], b_len: int) -> None:
    a_read = a_len - 1
    b_read = b_len - 1

    for a_write in range(len(a) - 1, -1, -1):
        if a_read >= 0 and b_read >= 0:
            if a[a_read] >= b[b_read]:
                a[a_write] = a[a_read]
                a_read -= 1
            else:
                a[a_write] = b[b_read]
                b_read -= 1
        elif a_read >= 0:
            a[a_write] = a[a_read]
            a_read -= 1
        elif b_read >= 0:
            a[a_write] = b[b_read]
            b_read -= 1
