from typing import Tuple, TypeVar, Generic, Optional, List
from linked_list import LinkedList, LinkedListNode

# TODO: how to choose hash table array size to guarantee O(1) access by key time?
# TODO: why array of linked lists not array of arrays?

KT = TypeVar("KT")
VT = TypeVar("VT")


class HashTable(Generic[KT, VT]):
    pointers: List[LinkedList[Tuple[KT, VT]]]

    def __init__(self) -> None:
        self.pointers = [None for i in range(0, 1000)]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, HashTable):
            return False

        if len(self.pointers) != len(other.pointers):
            return False

        for i in range(0, len(self.pointers)):
            if self.pointers[i] != other.pointers[i]:
                return False

        return True

    def set(self, key: KT, value: VT) -> None:
        index = hash(key) % len(self.pointers)

        if self.pointers[index] is None:
            self.pointers[index] = LinkedList(root=LinkedListNode(value=(key, value)))
        else:
            self.pointers[index].append((key, value))

    def get(self, key: KT) -> Optional[VT]:
        index = hash(key) % len(self.pointers)

        if self.pointers[index] is None:
            return None
        else:
            node = self.pointers[index].find(lambda v: v[0] == key)
            return node.value[1] if node else None

    def remove(self, key: KT) -> None:
        index = hash(key) % len(self.pointers)

        if self.pointers[index]:
            self.pointers[index].remove(lambda v: v[0] == key)
