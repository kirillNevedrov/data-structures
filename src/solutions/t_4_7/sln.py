from typing import List, Tuple
from src.graph import Graph, GraphNode
from src.queue import Queue


def get_build_order(
    projects: List[str], dependencies: List[Tuple[str, str]]
) -> List[str]:
    nodes_by_key = {p: GraphNode(value=p) for p in projects}

    for d in dependencies:
        depending_node = nodes_by_key[d[1]]
        dependency_node = nodes_by_key[d[0]]

        dependency_node.childs.append(depending_node)

    # calculate inboubt for each node
    nodes = nodes_by_key.values()
    for n in nodes:
        for c in n.childs:
            c.inbound += 1

    # add nodes with zero inbound to processing queue
    processing_queue = Queue[GraphNode]()
    for n in nodes:
        if n.inbound == 0:
            processing_queue.add(n)

    # add nodes to result array
    result = []
    while not processing_queue.is_empty():
        node = processing_queue.remove()

        for c in node.childs:
            c.inbound -= 1

            if c.inbound == 0:
                processing_queue.add(c)

        result.append(node.value)

    if len(result) != len(projects):
        raise Exception("Sorting is not possible because of cycle")

    return result
