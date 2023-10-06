from src.binary_search_tree import BinarySearchTree
from src.binary_tree import BinaryTreeNode
from .sln import get_all_posible_sequences


def test_returns_all_posible_sequences():
    # arrange
    tree = BinarySearchTree()

    tree.insert(3)
    tree.insert(7)
    tree.insert(9)
    tree.insert(5)
    tree.insert(1)

    # act
    sequences = get_all_posible_sequences(tree)

    # assert
    assert tree == BinarySearchTree(
        root=BinaryTreeNode(
            value=3,
            left=BinaryTreeNode(value=1),
            right=BinaryTreeNode(
                value=7,
                left=BinaryTreeNode(value=5),
                right=BinaryTreeNode(value=9),
            ),
        )
    )

    tuples = [tuple(s) for s in sequences]

    assert (3, 7,  9,  5,  1) in tuples

