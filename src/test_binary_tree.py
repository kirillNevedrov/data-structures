from .binary_tree import BinaryTree, BinaryTreeNode


def test_eq_returns_true_for_equal_tree():
    assert BinaryTree(
        root=BinaryTreeNode(
            value=1,
            left=BinaryTreeNode(
                value=2,
                left=BinaryTreeNode(value=4),
                right=BinaryTreeNode(value=5),
            ),
            right=BinaryTreeNode(value=3),
        )
    ) == BinaryTree(
        root=BinaryTreeNode(
            value=1,
            left=BinaryTreeNode(
                value=2,
                left=BinaryTreeNode(value=4),
                right=BinaryTreeNode(value=5),
            ),
            right=BinaryTreeNode(value=3),
        )
    )


def test_eq_returns_false_for_not_equal_tree():
    assert BinaryTree(
        root=BinaryTreeNode(
            value=1,
            left=BinaryTreeNode(
                value=2,
                left=BinaryTreeNode(value=4),
                right=BinaryTreeNode(value=5),
            ),
            right=BinaryTreeNode(value=3),
        )
    ) != BinaryTree(
        root=BinaryTreeNode(
            value=1,
            left=BinaryTreeNode(
                value=2,
                left=BinaryTreeNode(value=4),
                right=BinaryTreeNode(value=5),
            ),
            right=BinaryTreeNode(
                value=3,
                left=BinaryTreeNode(value=6),
            ),
        )
    )
