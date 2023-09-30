from src.graph import GraphNode
from .sln import is_tree_balanced


def test_returns_true_if_tree_is_balanced():
    # arrange
    root = GraphNode(value=0, childs=[None, None])
    node_1 = GraphNode(value=1, childs=[None, None])
    node_2 = GraphNode(value=2, childs=[None, None])
    node_3 = GraphNode(value=3, childs=[None, None])
    node_4 = GraphNode(value=4, childs=[None, None])

    root.childs = [node_1, node_2]
    node_1.childs = [node_3, node_4]

    # act
    # assert
    assert is_tree_balanced(root) == True


def test_returns_false_if_tree_is_not_balanced():
    # arrange
    root = GraphNode(value=0)
    node_1 = GraphNode(value=1, childs=[None, None])
    node_2 = GraphNode(value=2, childs=[None, None])
    node_3 = GraphNode(value=3, childs=[None, None])
    node_4 = GraphNode(value=4, childs=[None, None])
    node_5 = GraphNode(value=5, childs=[None, None])

    root.childs = [node_1, node_2]
    node_1.childs = [node_3, node_4]
    node_3.childs = [node_5, None]

    # act
    # assert
    assert is_tree_balanced(root) == False
