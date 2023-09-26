from .queue import Queue


def test_equals_returns_true_for_equal_queue():
    # arrange
    queue_1 = Queue()
    queue_1.add(2)
    queue_1.add(5)

    queue_2 = Queue()
    queue_2.add(2)
    queue_2.add(5)

    # act
    # assert
    assert queue_1 == queue_2


def test_equals_returns_false_for_not_equal_queue():
    # arrange
    queue_1 = Queue()
    queue_1.add(2)
    queue_1.add(5)

    queue_2 = Queue()
    queue_2.add(5)
    queue_2.add(2)

    # act
    # assert
    assert queue_1 != queue_2


def test_add_adds_item_to_end_of_queue():
    # arrange
    queue = Queue()

    # act
    queue.add(2)
    queue.add(5)

    # assert
    assert queue.first == Queue.QueueNode(data=2, next=Queue.QueueNode(data=5))
    assert queue.last == Queue.QueueNode(data=5)


def test_remove_removes_item_from_beginning_of_queue_and_returns_removed_item():
    # arrange
    queue = Queue()
    queue.add(2)
    queue.add(5)

    # act
    item = queue.remove()

    # assert
    assert queue.first == Queue.QueueNode(data=5)
    assert queue.last == Queue.QueueNode(data=5)
    assert item == 2


def test_peek_returns_item_from_beginning_of_queue():
    # arrange
    queue = Queue()
    queue.add(2)
    queue.add(5)

    # act
    item = queue.peek()

    # assert
    assert item == 2


def test_is_empty_returns_true_for_empty_queue():
    # arrange
    queue = Queue()

    # act
    # assert
    assert queue.is_empty() == True


def test_is_empty_returns_false_for_not_empty_queue():
    # arrange
    queue = Queue()
    queue.add(2)

    # act
    # assert
    assert queue.is_empty() == False
