from typing import List, Optional

from src.binary_search_tree import BinarySearchTree, BinaryTreeNode


def get_all_posible_sequences(tree: BinarySearchTree[int]) -> List[List[int]]:
    size = get_tree_size(tree.root)

    if not tree.root:
        return []

    nodes = []
    values = []
    add_child_nodes(nodes, tree.root)
    add_child_values(values, tree.root)

    return get_sequences_from_nodes(nodes, values, [[tree.root.value]], 1, size)


def get_sequences_from_nodes(
    nodes: List[BinaryTreeNode[int]],
    values: List[int],
    arrays: List[List[int]],
    level: int,
    size: int,
) -> List[List[int]]:
    new_arrays = []
    for a in arrays:
        for v in values:
            if v in a:
                continue

            new_array = a[:]
            new_array.append(v)
            new_arrays.append(new_array)

    new_nodes = []
    for node in nodes:
        add_child_nodes(nodes, node)
        add_child_values(values, node)

    return (
        get_sequences_from_nodes(new_nodes, values, new_arrays, level + 1, size)
        if level < size - 1
        else new_arrays
    )


def get_tree_size(node: BinaryTreeNode[int]) -> int:
    if not node:
        return 0

    left_tree_size = get_tree_size(node.left)
    right_tree_size = get_tree_size(node.right)

    return left_tree_size + right_tree_size + 1


def add_child_nodes(
    nodes: List[BinaryTreeNode[int]], node: Optional[BinaryTreeNode[int]]
):
    if node.left:
        nodes.append(node.left)

    if node.right:
        nodes.append(node.right)


def add_child_values(values: List[int], node: Optional[BinaryTreeNode[int]]):
    if node.left:
        values.append(node.left.value)

    if node.right:
        values.append(node.right.value)
