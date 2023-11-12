from typing import Optional
from .sln_1 import Solution, ListNode


def list_nodes_equal(node_1: Optional[ListNode], node_2: Optional[ListNode]) -> bool:
    if node_1 is None and node_2 is None:
        return True

    if node_1 is None or node_2 is None:
        return False

    return node_1.val == node_2.val and list_nodes_equal(node_1.next, node_2.next)


def test_sorts_list():
    assert list_nodes_equal(
        Solution().sortList(
            ListNode(
                val=10,
                next=ListNode(
                    val=1,
                    next=ListNode(val=30, next=ListNode(val=2, next=ListNode(val=5))),
                ),
            )
        ),
        ListNode(
            val=1,
            next=ListNode(
                val=2, next=ListNode(val=5, next=ListNode(val=10, next=ListNode(val=30)))
            ),
        ),
    )
