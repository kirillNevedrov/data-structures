from .sln import Queue


def test_rerutns_as_first_element_first_element_that_was_added():
    # arrange
    queue = Queue()

    # act
    queue.add(1)
    queue.add(5)

    item_1 = queue.remove()

    queue.add(3)

    item_2 = queue.remove()
    item_3 = queue.remove()

    # assert
    assert item_1 == 1
    assert item_2 == 5
    assert item_3 == 3
