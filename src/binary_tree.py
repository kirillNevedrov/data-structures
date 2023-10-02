from __future__ import annotations
from typing import Optional, TypeVar, Generic

T = TypeVar("T")


class BinaryTreeNode(Generic[T]):
    def __init__(
        self,
        value: T,
        left: Optional[BinaryTreeNode[T]] = None,
        right: Optional[BinaryTreeNode[T]] = None,
    ) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BinaryTreeNode):
            return False

        return (
            self.value == other.value
            and self.left == other.left
            and self.right == other.right
        )


class BinaryTree(Generic[T]):
    def __init__(self, root: Optional[BinaryTreeNode[T]] = None) -> None:
        self.root = root

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BinaryTree):
            return False

        return self.root == other.root
