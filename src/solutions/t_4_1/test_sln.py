from src.graph import GraphNode
from .sln import has_route

def test_returns_true_if_there_is_route_from_first_to_second_node():
    # arrange
    node_1 = GraphNode(value=1)
    node_2 = GraphNode(value=2)
    node_3 = GraphNode(value=3)
    node_4 = GraphNode(value=4)
    node_5 = GraphNode(value=5)

    node_1.childs = [node_2, node_3]
    node_2.childs = [node_3, node_4]
    node_4.childs = [node_5]

    # act
    # assert
    assert has_route(node_1, node_5) == True

def test_returns_true_if_there_is_route_from_first_to_second_node_in_graph_with_cycles():
    # arrange
    node_1 = GraphNode(value=1)
    node_2 = GraphNode(value=2)
    node_3 = GraphNode(value=3)
    node_4 = GraphNode(value=4)
    node_5 = GraphNode(value=5)

    node_1.childs = [node_2, node_3]
    node_2.childs = [node_3, node_4]
    node_3.childs = [node_1]
    node_4.childs = [node_5]

    # act
    # assert
    assert has_route(node_1, node_5) == True


def test_returns_false_if_there_is_no_route_from_first_to_second_node():
    # arrange
    node_1 = GraphNode(value=1)
    node_2 = GraphNode(value=2)
    node_3 = GraphNode(value=3)
    node_4 = GraphNode(value=4)
    node_5 = GraphNode(value=5)

    node_1.childs = [node_2, node_3]
    node_2.childs = [node_3, node_4]
    node_5.childs = [node_1]

    # act
    # assert
    assert has_route(node_1, node_5) == False