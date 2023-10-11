from abc import ABC, abstractmethod
from typing import List


class IPageBlock(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


class Page:
    def __init__(self, number: int, blocks: List[IPageBlock]) -> None:
        self.number = number
        self.blocks = blocks

    def render(self) -> str:
        return "".join(self.blocks)


class Bookmark:
    def __init__(self, page_number: int, title: str) -> None:
        self.page_number = page_number
        self.title = title


class Book:
    def __init__(self, pages: List[Page], bookmarks: List[Bookmark]) -> None:
        self.pages = pages
        self.bookmarks = bookmarks


class Shelf:
    def __init__(self, books: List[Book]) -> None:
        self.books = books
