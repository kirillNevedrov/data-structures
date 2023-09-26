from .stack import Stack


def test_equals_returns_true_for_equal_stack():
    # arrange
    stack_1 = Stack()
    stack_1.push(2)
    stack_1.push(5)

    stack_2 = Stack()
    stack_2.push(2)
    stack_2.push(5)

    # act
    # assert
    assert stack_1 == stack_2


def test_equals_returns_false_for_not_equal_stack():
    # arrange
    stack_1 = Stack()
    stack_1.push(2)
    stack_1.push(5)

    stack_2 = Stack()
    stack_2.push(5)
    stack_2.push(2)

    # act
    # assert
    assert stack_1 != stack_2


def test_push_adds_item_to_top_of_stack():
    # arrange
    stack = Stack()

    # act
    stack.push(2)
    stack.push(5)

    # assert
    assert stack.top == Stack.StackNode(data=5, next=Stack.StackNode(data=2))


def test_pop_removes_item_from_top_of_stack_and_returns_removed_item():
    # arrange
    stack = Stack()
    stack.push(2)
    stack.push(5)

    # act
    item = stack.pop()

    # assert
    assert stack.top == Stack.StackNode(data=2)
    assert item == 5

def test_peek_returns_item_from_top_of_stack():
    # arrange
    stack = Stack()
    stack.push(2)
    stack.push(5)

    # act
    item = stack.peek()

    # assert
    assert item == 5

def test_is_empty_returns_true_for_empty_stack():
    # arrange
    stack = Stack()

    # act
    # assert
    assert stack.is_empty() == True

def test_is_empty_returns_false_for_not_empty_stack():
    # arrange
    stack = Stack()
    stack.push(2)

    # act
    # assert
    assert stack.is_empty() == False
