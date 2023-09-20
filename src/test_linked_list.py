from linked_list import LinkedList, LinkedListNode


def test_equals_returns_true_for_equal_lists():
    assert LinkedList(
        root=LinkedListNode(
            value=1,
            next=LinkedListNode(
                value=2,
                next=LinkedListNode(value=3),
            ),
        )
    ) == LinkedList(
        root=LinkedListNode(
            value=1,
            next=LinkedListNode(
                value=2,
                next=LinkedListNode(value=3),
            ),
        )
    )


def test_equals_returns_false_for_not_equal_lists():
    assert LinkedList(
        root=LinkedListNode(
            value=1,
            next=LinkedListNode(
                value=2,
                next=LinkedListNode(value=3),
            ),
        )
    ) != LinkedList(
        root=LinkedListNode(
            value=1,
            next=LinkedListNode(
                value=2,
                next=LinkedListNode(value=4),
            ),
        )
    )


def test_append_appends_new_node():
    # arrange
    linked_list = LinkedList(root=LinkedListNode(value=1))

    # act
    linked_list.append(2)

    # assert
    assert linked_list == LinkedList(
        root=LinkedListNode(
            value=1,
            next=LinkedListNode(value=2),
        )
    )


def test_find_returns_node_by_value():
    assert LinkedList(
        root=LinkedListNode(
            value=1,
            next=LinkedListNode(
                value=2,
                next=LinkedListNode(value=3),
            ),
        )
    ).find(3) == LinkedListNode(value=3)

def test_find_returns_node_by_predicate():
    assert LinkedList(
        root=LinkedListNode(
            value=1,
            next=LinkedListNode(
                value=2,
                next=LinkedListNode(value=3),
            ),
        )
    ).find(lambda v: v == 3) == LinkedListNode(value=3)


def test_remove_removes_node_by_value():
    # arrange
    linked_list = LinkedList(
        root=LinkedListNode(
            value=1,
            next=LinkedListNode(
                value=2,
                next=LinkedListNode(value=3),
            ),
        )
    )

    # act
    linked_list.remove(2)

    # assert
    assert linked_list == LinkedList(
        root=LinkedListNode(
            value=1,
            next=LinkedListNode(value=3),
        )
    )

def test_remove_removes_node_by_predicate():
    # arrange
    linked_list = LinkedList(
        root=LinkedListNode(
            value=1,
            next=LinkedListNode(
                value=2,
                next=LinkedListNode(value=3),
            ),
        )
    )

    # act
    linked_list.remove(lambda v: v == 2)

    # assert
    assert linked_list == LinkedList(
        root=LinkedListNode(
            value=1,
            next=LinkedListNode(value=3),
        )
    )
