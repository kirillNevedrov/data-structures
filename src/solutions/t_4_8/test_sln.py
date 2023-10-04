from .sln import get_first_common_ancestor
from src.binary_tree import BinaryTreeNode


def test_returns_first_common_ancestor_node_if_it_exists():
    # arrange
    node_1 = BinaryTreeNode(value=2)
    node_2 = BinaryTreeNode(value=2)
    fca_node = BinaryTreeNode(
        value=6,
        left=node_2,
        right=BinaryTreeNode(
            value=44,
            left=BinaryTreeNode(
                value=55,
                left=node_1,
            ),
            right=BinaryTreeNode(value=100),
        ),
    )
    root = BinaryTreeNode(
        value=1,
        left=fca_node,
        right=BinaryTreeNode(value=1),
    )

    # act
    # assert
    assert (
        get_first_common_ancestor(root=root, node_1=node_1, node_2=node_2) is fca_node
    )


def test_returns_null_if_first_common_ancestor_node_does_not_exist():
    # arrange
    node_1 = BinaryTreeNode(value=2)
    node_2 = BinaryTreeNode(value=2)
    root = BinaryTreeNode(
        value=1,
        left=BinaryTreeNode(
            value=6,
            left=BinaryTreeNode(value=2),
            right=BinaryTreeNode(
                value=44,
                left=BinaryTreeNode(
                    value=55,
                    left=node_1,
                ),
                right=BinaryTreeNode(value=100),
            ),
        ),
        right=BinaryTreeNode(value=1),
    )

    # act
    # assert
    assert get_first_common_ancestor(root=root, node_1=node_1, node_2=node_2) is None
