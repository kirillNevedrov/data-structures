from src.linked_list import LinkedList, LinkedListNode
from .sln import remove_duplicates


def test_removes_suplicates():
    # arrange
    list = LinkedList(
        root=LinkedListNode(
            value=1,
            next=LinkedListNode(
                value=0,
                next=LinkedListNode(
                    value=1,
                    next=LinkedListNode(value=100),
                ),
            ),
        )
    )

    # act
    remove_duplicates(list)

    # assert
    list == LinkedList(
        root=LinkedListNode(
            value=1,
            next=LinkedListNode(
                value=0,
                next=LinkedListNode(value=100),
            ),
        )
    )
