from __future__ import annotations
from typing import TypeVar, Generic, Optional, Callable, Union

T = TypeVar("T")


class LinkedListNode(Generic[T]):
    value: T
    next: Optional[LinkedListNode[T]]

    def __init__(self, value: T, next: Optional[LinkedListNode[T]] = None) -> None:
        self.value = value
        self.next = next

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, LinkedListNode):
            return False

        return self.value == other.value and self.next == other.next


class LinkedList(Generic[T]):
    root: Optional[LinkedListNode[T]]

    def __init__(self, root: Optional[LinkedListNode[T]] = None) -> None:
        self.root = root

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, LinkedList):
            return False

        return self.root == other.root

    def append(self, value: T) -> None:
        if not self.root:
            self.root = LinkedListNode(value=value)
            return

        current_node = self.root

        while current_node.next:
            current_node = current_node.next

        current_node.next = LinkedListNode(value=value)

    def find(self, value: Union[T, Callable[[T], bool]]) -> Optional[LinkedListNode[T]]:
        current_node = self.root
        is_callable = callable(value)

        while current_node:
            if is_callable:
                if value(current_node.value):
                    return current_node
            else:
                if current_node.value == value:
                    return current_node

            current_node = current_node.next

        return None

    def remove(self, value: T) -> None:
        prev_node = None
        current_node = self.root

        while current_node:
            if current_node.value == value:
                if prev_node:
                    prev_node.next = current_node.next
                else:
                    self.root = current_node.next
                return

            prev_node = current_node
            current_node = current_node.next
