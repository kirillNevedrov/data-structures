from __future__ import annotations
from enum import Enum
from typing import List, Tuple

from src.queue import Queue


class GameState(Enum):
    RESET = "RESET"
    PENDING = "PENDING"
    SUCCEED = "SUCCEED"
    FAILED = "FAILED"


class Block:
    def __init__(self) -> None:
        self.is_open = False
        self.is_flagged = False

    def open(self, x: int, y: int, game: Game) -> None:
        self.is_open = True

    def flag(self) -> None:
        self.is_flagged = True


class BombBlock(Block):
    def open(self, x: int, y: int, game: Game) -> None:
        super().open(x, y, game)

        game.state = GameState.FAILED


class NumberBlock(Block):
    def __init__(self, number: int) -> None:
        super().__init__()

        self.number = number


class EmptyBlock(Block):
    def open(self, x: int, y: int, game: Game) -> None:
        coords_queue = Queue[Tuple[int, int]]()

        coords_queue.add((x, y))

        while not coords_queue.is_empty():
            c = coords_queue.remove()

            index = c[1] * game.width + c[0]

            if index < 0 or index > len(game.blocks) - 1:
                continue

            b = game.blocks[index]

            if not b.is_open:
                if isinstance(b, EmptyBlock):
                    b.open_empty_block(
                        x=c[0], y=c[1], game=game, coords_queue=coords_queue
                    )
                elif isinstance(b, NumberBlock):
                    b.open(x=c[0], y=c[1], game=game)

    def open_empty_block(
        self, x: int, y: int, game: Game, coords_queue: Queue[Tuple[int, int]]
    ) -> None:
        super().open(x, y, game)

        coords_queue.add((x - 1, y - 1))
        coords_queue.add((x - 1, y))
        coords_queue.add((x - 1, y + 1))
        coords_queue.add((x, y - 1))
        coords_queue.add((x, y + 1))
        coords_queue.add((x + 1, y - 1))
        coords_queue.add((x + 1, y))
        coords_queue.add((x + 1, y + 1))


class Game:
    def __init__(self, blocks: List[Block], width: int) -> None:
        self.blocks = blocks
        self.width = width
        self.state = GameState.RESET

    def open(self, x: int, y: int) -> None:
        if self.state == GameState.RESET:
            self.state = GameState.PENDING

        index = y * self.width + x

        if index > len(self.blocks) - 1:
            raise Exception("Block with x: {x}, y: {y} not found")

        block = self.blocks[index]

        block.open(x=x, y=y, game=self)

        if self.state == GameState.PENDING:
            is_every_non_bomb_block_open = True
            for b in self.blocks:
                if not isinstance(b, BombBlock) and not b.is_open:
                    is_every_non_bomb_block_open = False
                    break

            if is_every_non_bomb_block_open:
                self.state = GameState.SUCCEED

    def flag(self, x: int, y: int) -> None:
        if self.state == GameState.RESET:
            self.state = GameState.PENDING

        index = y * self.width + x

        if index > len(self.blocks) - 1:
            raise Exception("Block with x: {x}, y: {y} not found")

        block = self.blocks[index]

        block.flag()

    def reset(self, blocks: List[Block], width: int) -> None:
        self.blocks = blocks
        self.width = width
        self.state = GameState.RESET
