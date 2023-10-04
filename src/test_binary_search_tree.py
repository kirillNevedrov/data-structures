from .binary_search_tree import BinarySearchTree, BinaryTreeNode


def test_insert_inserts_new_value_maintaining_sort_order():
    # arrange
    tree = BinarySearchTree()

    # act
    tree.insert(3)
    tree.insert(7)
    tree.insert(9)
    tree.insert(5)
    tree.insert(1)

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


def test_remove_removes_value_maintaining_sort_order():
    # arrange
    tree = BinarySearchTree()

    tree.insert(3)
    tree.insert(7)
    tree.insert(9)
    tree.insert(5)
    tree.insert(1)

    # act
    tree.remove(7)

    # assert
    assert tree == BinarySearchTree(
        root=BinaryTreeNode(
            value=3,
            left=BinaryTreeNode(value=1),
            right=BinaryTreeNode(
                value=5,
                right=BinaryTreeNode(value=9),
            ),
        )
    )


def test_search_returns_node_if_node_exists():
    # arrange
    tree = BinarySearchTree()

    tree.insert(3)
    tree.insert(7)
    tree.insert(9)
    tree.insert(5)
    tree.insert(1)

    # act
    # assert
    assert tree.search(7) == BinaryTreeNode(
        value=7,
        left=BinaryTreeNode(value=5),
        right=BinaryTreeNode(value=9),
    )
