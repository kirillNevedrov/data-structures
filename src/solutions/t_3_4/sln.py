from __future__ import annotations
from typing import TypeVar, Generic, Optional
from src.stack import Stack, EmptyStackException

T = TypeVar("T")


class EmptyQueueException(Exception):
    ...


class Queue(Generic[T]):
    def __init__(self) -> None:
        self.first = Stack[T]()
        self.second = Stack[T]()

    def add(self, item: T) -> None:
        self.first.push(item)

    def remove(self) -> T:
        if self.second.is_empty():
            self.__copy_stack(self.first, self.second)

        if self.second.is_empty():
            raise EmptyQueueException

        return self.second.pop()

    def peek(self) -> T:
        if self.second.is_empty():
            self.__copy_stack(self.first, self.second)

        if self.second.is_empty():
            raise EmptyQueueException

        return self.second.peek()

    def is_empty(self) -> bool:
        return self.first.is_empty() and self.second.is_empty()

    def __copy_stack(self, src: Stack[T], trg: Stack[T]):
        while True:
            try:
                i = src.pop()
                trg.push(i)
            except EmptyStackException:
                break
