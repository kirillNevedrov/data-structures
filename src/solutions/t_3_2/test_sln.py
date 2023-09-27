from .sln import Stack, EmptyStackException


def test_min_returns_min_stack_value():
    # arrange
    stack = Stack()
    stack.push(2)
    stack.push(4)
    stack.push(1)
    stack.push(6)

    # act
    mins = []
    while True:
        try:
            mins.append(stack.min())
            stack.pop()
        except EmptyStackException:
            break

    # assert
    assert mins == [1, 1, 2, 2]
