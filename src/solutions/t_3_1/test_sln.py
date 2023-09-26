from .sln import Stack

def test_push_adds_item_to_top_of_stack():
    # arrange
    array = []

    stack_1 = Stack(array=array, index=0)
    stack_2 = Stack(array=array, index=1)
    stack_3 = Stack(array=array, index=2)

    # act
    stack_1.push(2)
    stack_1.push(5)

    stack_2.push(9)
    stack_2.push(11)

    stack_3.push(16)
    stack_3.push(21)

    # assert
    assert array == [2, 9, 16, 5, 11, 21]


def test_pop_removes_item_from_top_of_stack_and_returns_removed_item():
    # arrange
    array = []

    stack_1 = Stack(array=array, index=0)
    stack_2 = Stack(array=array, index=1)
    stack_3 = Stack(array=array, index=2)

    stack_1.push(2)
    stack_1.push(5)

    stack_2.push(9)
    stack_2.push(11)

    stack_3.push(16)
    stack_3.push(21)

    # act
    item_1 = stack_1.pop()
    item_2 = stack_2.pop()
    item_3 = stack_3.pop()

    # assert
    assert array == [2, 9, 16, None, None, None]

    assert item_1 == 5
    assert item_2 == 11
    assert item_3 == 21
