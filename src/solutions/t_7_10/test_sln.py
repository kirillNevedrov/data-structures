from .sln import Game, BombBlock, GameState, NumberBlock, EmptyBlock


def test_failed_if_open_bobmb_block():
    # arrange
    game = Game(
        blocks=[
            NumberBlock(number=1), EmptyBlock(), EmptyBlock(), NumberBlock(number=1), NumberBlock(number=1),
            NumberBlock(number=2), BombBlock(), EmptyBlock(), BombBlock(), NumberBlock(number=1),
            BombBlock(), EmptyBlock(), EmptyBlock(), NumberBlock(1), NumberBlock(number=1),
            BombBlock(), NumberBlock(2), EmptyBlock(), EmptyBlock(), EmptyBlock(),
        ],
        width=5,
    )

    # act
    game.open(x=1, y=1)

    # assert
    assert game.state == GameState.FAILED

def test_pending_if_open_not_all_blocks():
    # arrange
    game = Game(
        blocks=[
            NumberBlock(number=1), EmptyBlock(), EmptyBlock(), NumberBlock(number=1), NumberBlock(number=1),
            NumberBlock(number=2), BombBlock(), EmptyBlock(), BombBlock(), NumberBlock(number=1),
            BombBlock(), EmptyBlock(), EmptyBlock(), NumberBlock(1), NumberBlock(number=1),
            BombBlock(), NumberBlock(2), EmptyBlock(), EmptyBlock(), EmptyBlock(),
        ],
        width=5,
    )

    # act
    game.open(x=0, y=0)
    game.open(x=1, y=0)
    game.open(x=4, y=0)

    # assert
    assert game.state == GameState.PENDING

def test_succeed_if_open_all_blocks_except_bomb():
    # arrange
    game = Game(
        blocks=[
            NumberBlock(number=1), EmptyBlock(), EmptyBlock(), NumberBlock(number=1), NumberBlock(number=1),
            NumberBlock(number=2), BombBlock(), EmptyBlock(), BombBlock(), NumberBlock(number=1),
            BombBlock(), EmptyBlock(), EmptyBlock(), NumberBlock(1), NumberBlock(number=1),
            BombBlock(), NumberBlock(2), EmptyBlock(), EmptyBlock(), EmptyBlock(),
        ],
        width=5,
    )

    # act
    game.open(x=0, y=0)
    game.open(x=1, y=0)
    game.open(x=4, y=0)
    game.open(x=4, y=1)

    # assert
    assert game.state == GameState.SUCCEED
