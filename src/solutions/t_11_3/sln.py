from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from src.binary_tree import BinaryTree, BinaryTreeNode


@dataclass
class NodeValue:
    number: int
    count: int
    left_subtree_count: int


class BinarySearchTree(BinaryTree[NodeValue]):
    def __init__(self, root: Optional[BinaryTreeNode[NodeValue]] = None) -> None:
        super().__init__(root)

    def insert(self, number: int) -> None:
        node = BinaryTreeNode(
            value=NodeValue(number=number, count=1, left_subtree_count=0)
        )

        if self.root is None:
            self.root = node
        else:
            insert_node(self.root, node)

    def get_rank(self, number: int) -> Optional[int]:
        return get_rank(self.root, number, 0)


def insert_node(
    current_node: BinaryTreeNode[NodeValue], node: BinaryTreeNode[NodeValue]
) -> None:
    if node.value.number == current_node.value.number:
        current_node.value.count += 1
    elif node.value.number < current_node.value.number:
        current_node.value.left_subtree_count += 1

        if current_node.left:
            insert_node(current_node.left, node)
        else:
            current_node.left = node
    else:
        if current_node.right:
            insert_node(current_node.right, node)
        else:
            current_node.right = node


def get_rank(
    current_node: BinaryTreeNode[NodeValue], number: int, left_subtree_count: int
) -> Optional[int]:
    if current_node is None:
        return None

    if current_node.value.number == number:
        return (
            left_subtree_count
            + current_node.value.left_subtree_count
            + current_node.value.count
            - 1
        )

    if number < current_node.value.number:
        return get_rank(current_node.left, number, left_subtree_count)
    else:
        return get_rank(
            current_node.right,
            number,
            left_subtree_count + 1 + current_node.value.left_subtree_count,
        )


class RankCalculator:
    def __init__(self) -> None:
        self._tree = BinarySearchTree()

    def track(self, number: int) -> None:
        self._tree.insert(number)

    def get_rank(self, number: int) -> Optional[int]:
        return self._tree.get_rank(number)
