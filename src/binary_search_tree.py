from __future__ import annotations
from typing import Optional, TypeVar

from .binary_tree import BinaryTree, BinaryTreeNode

T = TypeVar("T")


class BinarySearchTree(BinaryTree[T]):
    def __init__(self, root: Optional[BinaryTreeNode[T]] = None) -> None:
        super().__init__(root)

    def insert(self, value: T) -> None:
        node = BinaryTreeNode(value=value)

        if self.root is None:
            self.root = node
        else:
            insert_node(self.root, node)

    def remove(self, value: T) -> None:
        if self.root is None:
            return
        else:
            remove(self, None, self.root, value)


def insert_node(current_node: BinaryTreeNode[T], node: BinaryTreeNode[T]) -> None:
    left = current_node.left
    right = current_node.right

    if node.value <= current_node.value:
        if left:
            insert_node(left, node)
        else:
            current_node.left = node
    else:
        if right:
            insert_node(right, node)
        else:
            current_node.right = node


def remove(
    tree: BinaryTree[T],
    parent_node: Optional[BinaryTreeNode[T]],
    current_node: BinaryTreeNode[T],
    value: T,
) -> None:
    if current_node.value == value:
        if parent_node:
            if current_node is parent_node.left:
                parent_node.left = None
            else:
                parent_node.right = None

            if current_node.left:
                insert_node(tree.root, current_node.left)

            if current_node.right:
                insert_node(tree.root, current_node.right)
        else:
            if current_node.left and current_node.right:
                tree.root = current_node.left

                insert_node(tree.root, current_node.right)
            elif current_node.left:
                tree.root = current_node.left
            elif current_node.right:
                tree.root = current_node.right

    elif value < current_node.value and current_node.left:
        remove(tree, current_node, current_node.left, value)
    elif value > current_node.value and current_node.right:
        remove(tree, current_node, current_node.right, value)
