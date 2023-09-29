from src.graph import Graph, GraphNode
from src.queue import Queue

def has_route(src_node: GraphNode, trg_node: GraphNode) -> bool:
    queue = Queue[GraphNode]()
    src_node.visited = True
    queue.add(src_node)

    while not queue.is_empty():
        n = queue.remove()

        if n is trg_node:
            return True
        
        for c in n.childs:
            if not c.visited:
                c.visited = True
                queue.add(c)

    return False

# def has_route(src_node: GraphNode, trg_node: GraphNode) -> bool:
#     if src_node is None or trg_node is None:
#         return False

#     if src_node is trg_node:
#         return True

#     src_node.visited = True

#     for c in src_node.childs:
#         if not c.visited:
#             if has_route(c, trg_node):
#                 return True

#     return False
