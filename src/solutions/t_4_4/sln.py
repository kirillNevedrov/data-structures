from src.graph import GraphNode


class NodeIsNotBalancedError(Exception):
    ...


def is_tree_balanced(root: GraphNode) -> bool:
    if root is None:
        return True

    try:
        return is_node_balanced(get_height(root.childs[0]), get_height(root.childs[1]))
    except NodeIsNotBalancedError:
        return False


def get_height(node: GraphNode) -> int:
    if node is None:
        return 0

    left_height = get_height(node.childs[0])
    right_height = get_height(node.childs[1])

    if not is_node_balanced(left_height, right_height):
        raise NodeIsNotBalancedError

    return max(left_height, right_height) + 1


def is_node_balanced(left_height: int, right_height: int) -> bool:
    return abs(left_height - right_height) <= 1
