from __future__ import annotations
from typing import TypeVar, Generic, Optional

T = TypeVar("T")


class EmptyStackException(Exception):
    ...


class Stack(Generic[T]):
    class StackNode(Generic[T]):
        def __init__(
            self, data: T, min: T, next: Optional[Stack.StackNode[T]] = None
        ) -> None:
            self.data = data
            self.min = min
            self.next = next

        def __eq__(self, other: object) -> bool:
            if not isinstance(other, Stack.StackNode):
                return False

            return self.data == other.data and self.next == other.next

    def __init__(self) -> None:
        self.top: Optional[Stack.StackNode[T]] = None

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Stack):
            return False

        return self.top == other.top

    def push(self, item: T) -> None:
        if self.top is None:
            min_item = item
        else:
            min_item = min(self.top.min, item)

        t = self.StackNode(data=item, min=min_item, next=self.top)

        self.top = t

    def pop(self) -> T:
        if self.top is None:
            raise EmptyStackException

        item = self.top.data
        self.top = self.top.next

        return item

    def min(self) -> T:
        if self.top is None:
            raise EmptyStackException

        return self.top.min

    def peek(self) -> T:
        if self.top is None:
            raise EmptyStackException

        return self.top.data

    def is_empty(self) -> bool:
        return self.top is None
