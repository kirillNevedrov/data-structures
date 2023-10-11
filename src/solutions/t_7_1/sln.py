from enum import Enum
from typing import List, Optional, TypeVar, Generic


class CardSuit(Enum):
    SPADES = "SPADES"
    CLUBS = "CLUBS"
    HEARTS = "HEARTS"
    DIAMONDS = "DIAMONDS"


class Card:
    def __init__(self, suit: CardSuit, rank: int) -> None:
        self.suit = suit
        self.rank = rank


T = TypeVar("T", bound=Card)


class DeckOfCards(Generic[T]):
    def __init__(self, cards: List[T]) -> None:
        self.cards = cards

    def get_card(self, index: int) -> Optional[T]:
        return self.cards[index] if index <= len(self.cards) - 1 else None
