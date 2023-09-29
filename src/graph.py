from __future__ import annotations
from typing import List, TypeVar, Generic

T = TypeVar("T")


class GraphNode(Generic[T]):
    def __init__(self, value: T, childs: List[GraphNode[T]] = [], visited: bool = False) -> None:
        self.value = value
        self.childs = childs
        self.visited = visited


class Graph(Generic[T]):
    def __init__(self, nodes: List[GraphNode[T]] = []) -> None:
        self.nodes = nodes
        
