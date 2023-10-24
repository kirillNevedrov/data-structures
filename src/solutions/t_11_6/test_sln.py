from .sln import RankCalculator

def test_calculates_rank_of_every_tracked_number():
    # arrange
    stream = [5, 1, 4, 4, 5, 9, 7, 13, 3]
    calculator = RankCalculator()
    
    # act
    for n in stream:
        calculator.track(n)

    # assert
    assert calculator.get_rank(1) == 0
    assert calculator.get_rank(3) == 1
    assert calculator.get_rank(4) == 3