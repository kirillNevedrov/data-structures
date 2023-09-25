from typing import Optional
from src.linked_list import LinkedList, LinkedListNode


def detect_loop(list: LinkedList) -> Optional[LinkedListNode]:
    slow  = list.root
    fast = list.root

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            break

    if fast is None or fast.next is None:
        return None
    
    slow = list.root
    while slow is not fast:
        slow = slow.next
        fast = fast.next

    return fast


# def detect_loop(list: LinkedList) -> Optional[LinkedListNode]:
#     mark_node = LinkedListNode(value=None)

#     node = list.root
#     while node:
#         if node.next == mark_node:
#             return node

#         next_node = node.next
#         node.next = mark_node
#         node = next_node

#     return None
