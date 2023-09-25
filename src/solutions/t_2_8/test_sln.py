from src.linked_list import LinkedList, LinkedListNode
from .sln import detect_loop


def test_detects_loop_if_loop_exists():
    last_loop_node = LinkedListNode(value=100)
    first_loop_node = LinkedListNode(
        value=10,
        next=LinkedListNode(
            value=6,
            next=LinkedListNode(value=3, next=last_loop_node),
        ),
    )
    last_loop_node.next = first_loop_node

    assert (
        detect_loop(LinkedList(root=LinkedListNode(value=1, next=first_loop_node)))
        is first_loop_node
    )


def test_does_not_detect_loop_if_loop_does_not_exist():
    assert (
        detect_loop(
            LinkedList(
                root=LinkedListNode(
                    value=1,
                    next=LinkedListNode(
                        value=10,
                        next=LinkedListNode(
                            value=6,
                            next=LinkedListNode(
                                value=3,
                                next=LinkedListNode(value=100),
                            ),
                        ),
                    ),
                )
            )
        )
        is None
    )
