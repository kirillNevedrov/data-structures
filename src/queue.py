from __future__ import annotations
from typing import TypeVar, Generic, Optional

T = TypeVar("T")


class EmptyQueueException(Exception):
    ...


class Queue(Generic[T]):
    class QueueNode(Generic[T]):
        def __init__(self, data: T, next: Optional[Queue.QueueNode[T]] = None) -> None:
            self.data = data
            self.next = next

        def __eq__(self, other: object) -> bool:
            if not isinstance(other, Queue.QueueNode):
                return False

            return self.data == other.data and self.next == other.next

    def __init__(self) -> None:
        self.first: Optional[Queue.QueueNode[T]] = None
        self.last: Optional[Queue.QueueNode[T]] = None

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Queue):
            return False

        return self.first == other.first

    def add(self, item: T) -> None:
        t = self.QueueNode(data=item)

        if self.last:
            self.last.next = t

        self.last = t

        if self.first is None:
            self.first = self.last

    def remove(self) -> T:
        if self.first is None:
            raise EmptyQueueException

        item = self.first.data
        self.first = self.first.next

        if self.first is None:
            self.last = None

        return item

    def peek(self) -> T:
        if self.first is None:
            raise EmptyQueueException

        return self.first.data

    def is_empty(self) -> bool:
        return self.first is None
