from __future__ import annotations
from typing import TypeVar, Generic, Optional

T = TypeVar("T")


class LinkedListNode(Generic[T]):
    value: T
    next: Optional[LinkedListNode[T]]

    def __init__(self, value: T, next: Optional[LinkedListNode[T]] = None) -> None:
        self.value = value
        self.next = next


class LinkedList(Generic[T]):
    root: LinkedListNode[T]

    def __init__(self, root: LinkedListNode[T]) -> None:
        self.root = root

    def append(self, value: T) -> None:
        current_node = self.root

        while current_node.next:
            current_node = current_node.next

        current_node.next = LinkedListNode(value=value)

    def find(self, value: T) -> Optional[LinkedListNode[T]]:
        current_node = self.root

        while True:
            if current_node.value == value:
                return current_node

            if current_node.next:
                current_node = current_node.next
            else:
                break

        return None

    def remove(self, value: T) -> None:
        prev_node = None
        current_node = self.root

        while True:
            if current_node.value == value:
                if prev_node:
                    prev_node.next = current_node.next
                else:
                    self.root = current_node.next

            if current_node.next:
                prev_node = current_node
                current_node = current_node.next
            else:
                break
