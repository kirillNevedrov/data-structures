from .sln import insert_number


def test_inserts_number():
    assert insert_number(n=0b10000000000, m=0b10011, i=2, j=6) == 0b10001001100
