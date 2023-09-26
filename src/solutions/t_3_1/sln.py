from __future__ import annotations
from typing import List, TypeVar, Generic

T = TypeVar("T")


class EmptyStackException(Exception):
    ...


class Stack(Generic[T]):
    def __init__(self, array: List[T], index: int) -> None:
        self.number_of_stacks = 3
        self.array = array
        self.index = index
        self.size = 0

    def push(self, item: T) -> None:
        self.size += 1
        item_index = self.__get_top_index()

        item_index_offset = item_index - (len(self.array) - 1)
        if item_index_offset > 0:
            self.array += [None] * item_index_offset

        self.array[item_index] = item

    def pop(self) -> T:
        if self.size == 0:
            raise EmptyStackException

        item_index = self.__get_top_index()

        item = self.array[item_index]
        self.array[item_index] = None
        self.size -= 1

        return item

    def peek(self) -> T:
        if self.size == 0:
            raise EmptyStackException

        item_index = self.__get_top_index()

        return self.array[item_index]

    def is_empty(self) -> bool:
        return self.size == 0

    def __get_top_index(self) -> int:
        return ((self.size - 1) * self.number_of_stacks) + self.index
