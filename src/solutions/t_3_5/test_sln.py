from src.stack import Stack

from .sln import sort


def test_sorts_stack():
    # arrange
    stack = Stack[int]()
    stack.push(3)
    stack.push(1)
    stack.push(6)
    stack.push(2)

    # act
    sort(stack)

    # assert
    assert stack.pop() == 1
    assert stack.pop() == 2
    assert stack.pop() == 3
    assert stack.pop() == 6
