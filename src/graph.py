from __future__ import annotations
from typing import List, TypeVar, Generic

T = TypeVar("T")


class GraphNode(Generic[T]):
    def __init__(
        self,
        value: T,
        childs: List[GraphNode[T]] = None,
        visited: bool = False,
        inbound: int = 0,
    ) -> None:
        if childs is None:
            childs = []

        self.value = value
        self.childs = childs
        self.visited = visited
        self.inbound = inbound


class Graph(Generic[T]):
    def __init__(self, nodes: List[GraphNode[T]] = None) -> None:
        if nodes is None:
            nodes = []

        self.nodes = nodes
