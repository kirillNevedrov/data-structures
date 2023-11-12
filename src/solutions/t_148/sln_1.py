from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self) -> None:
        self.tail = ListNode()
        self.next_sub_list = ListNode()

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        n = self.get_count(head)
        start = head
        dummy_head = ListNode()
        size = 1

        while size < n:
            self.tail = dummy_head
            while start:
                if start.next is None:
                    self.tail.next = start
                    break

                mid = self.split(start, size)
                self.merge(start, mid)
                start = self.next_sub_list
            start = dummy_head.next

            size *= 2

        return dummy_head.next

    def split(self, start: ListNode, size: int) -> ListNode:
        mid_prev = start
        end: ListNode = start.next

        # use fast and slow approach to find middle and end of second linked list
        index = 1
        while index < size and (mid_prev.next or end.next):
            if end.next:
                end = end.next.next if end.next.next else end.next

            if mid_prev.next:
                mid_prev = mid_prev.next

            index += 1

        mid = mid_prev.next
        mid_prev.next = None
        self.next_sub_list = end.next
        end.next = None

        return mid

    def merge(self, list_1: ListNode, list_2: ListNode) -> None:
        dummy_head = ListNode()
        new_tail = dummy_head

        while list_1 and list_2:
            if list_1.val < list_2.val:
                new_tail.next = list_1
                list_1 = list_1.next
                new_tail = new_tail.next
            else:
                new_tail.next = list_2
                list_2 = list_2.next
                new_tail = new_tail.next

        new_tail.next = list_1 if list_1 else list_2

        # traverse till the end of merged list to get the newTail
        while new_tail.next:
            new_tail = new_tail.next

        # link the old tail with the head of merged list
        self.tail.next = dummy_head.next

        # update the old tail to the new tail of merged list
        self.tail = new_tail

    def get_count(self, head: ListNode) -> int:
        cnt = 0
        ptr = head

        while ptr:
            ptr = ptr.next
            cnt += 1

        return cnt
