from typing import Optional
from src.binary_tree import BinaryTreeNode
from src.queue import Queue


def get_first_common_ancestor(
    root: BinaryTreeNode[int], node_1: BinaryTreeNode[int], node_2: BinaryTreeNode[int]
) -> Optional[BinaryTreeNode[int]]:
    return get_next_fca(
        current_node=root, current_fca=None, node_1=node_1, node_2=node_2
    )


def get_next_fca(
    current_node: BinaryTreeNode[int],
    current_fca: Optional[BinaryTreeNode[int]],
    node_1: BinaryTreeNode[int],
    node_2: BinaryTreeNode[int],
) -> Optional[BinaryTreeNode[int]]:
    if current_node is None:
        return current_fca

    is_node_1_ancestor = is_node_ancestor(ancestor_node=current_node, node=node_1)
    is_node_2_ancestor = is_node_ancestor(ancestor_node=current_node, node=node_2)

    if is_node_1_ancestor and is_node_2_ancestor:
        return get_next_fca(
            current_node=current_node.left,
            current_fca=current_node,
            node_1=node_1,
            node_2=node_2,
        )
    elif current_fca and current_node is current_fca.left:
        return get_next_fca(
            current_node=current_fca.right,
            current_fca=current_fca,
            node_1=node_1,
            node_2=node_2,
        )
    else:
        return current_fca


def is_node_ancestor(
    ancestor_node: BinaryTreeNode[int], node: BinaryTreeNode[int]
) -> bool:
    queue = Queue[BinaryTreeNode[int]]()

    if ancestor_node.left:
        queue.add(ancestor_node.left)
    if ancestor_node.right:
        queue.add(ancestor_node.right)

    while not queue.is_empty():
        current_node = queue.remove()

        if current_node is node:
            return True

        if current_node.left:
            queue.add(current_node.left)
        if current_node.right:
            queue.add(current_node.right)

    return False
