from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        mid = self.get_mid(head)
        left = self.sortList(head)
        right = self.sortList(mid)

        return self.merge(left, right)

    def merge(self, list_1: ListNode, list_2: ListNode) -> ListNode:
        dummy_head = ListNode()
        tail = dummy_head

        while list_1 and list_2:
            if list_1.val < list_2.val:
                tail.next = list_1
                list_1 = list_1.next
                tail = tail.next
            else:
                tail.next = list_2
                list_2 = list_2.next
                tail = tail.next

        tail.next = list_1 if list_1 else list_2

        return dummy_head.next

    def get_mid(self, head: ListNode) -> ListNode:
        mid_prev = None
        while head and head.next:
            mid_prev = head if mid_prev is None else mid_prev.next
            head = head.next.next

        mid = mid_prev.next
        mid_prev.next = None

        return mid
