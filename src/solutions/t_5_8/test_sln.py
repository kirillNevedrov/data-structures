from .sln import draw_line


def test_draws_line_from_x_1_y_to_x_2_y():
    # arrange
    screen = bytearray([
        1, 5, 19, 4, 
        9, 30, 62, 1, 
        82, 6, 34, 18, 
        5, 8, 72, 150,
        230, 0, 67, 255
    ])

    # act
    draw_line(screen=screen, width=32, x_1=10,x_2=30,y=2)

    # assert
    assert screen == bytearray([
        1, 5, 19, 4, 
        9, 30, 62, 1, 
        82, 63, 255, 254, 
        5, 8, 72, 150,
        230, 0, 67, 255
    ])
