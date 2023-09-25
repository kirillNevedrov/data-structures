from src.linked_list import LinkedList, LinkedListNode
from .sln import partition


def test_partitions_list():
    # arrange
    list = LinkedList(
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

    # act
    partition(list, 5)

    # assert
    list == LinkedList(
        root=LinkedListNode(
            value=1,
            next=LinkedListNode(
                value=3,
                next=LinkedListNode(
                    value=10,
                    next=LinkedListNode(
                        value=6,
                        next=LinkedListNode(value=100),
                    ),
                ),
            ),
        )
    )
