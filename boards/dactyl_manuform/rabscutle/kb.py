import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
#from kmk.quickpin.pro_micro.avr_promicro import translate as avr
from kmk.quickpin.pro_micro.boardsource_blok import pinout as pins
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    row_pins = (
        board.GP04, board.GP05, board.GP06, board.GP07, board.GP08, board.GP09
    )
    col_pins = (
        board.GP26, board.GP22, board.GP20, board.GP23, board.GP21
    )
    diode_orientation = DiodeOrientation.ROWS
    data_pin = board.TX
    # data_pin2 =
    # rgb_pixel_pin = pins[avr['D3']]
    # num_pixels = 12

    # flake8: noqa
    # fmt: off
    coord_mapping = [
        0, 5, 10, 15, 20, 25,           55, 50, 45, 40, 35, 30,
        1, 6, 11, 16, 21, 26,           56, 51, 46, 41, 36, 31,
        2, 7, 12, 17, 22, 27,           57, 52, 47, 42, 37, 32,
              13, 18,                           48, 43,
        4, 9, 14, 19, 24, 29,           59, 54, 49, 44, 39, 34
    ]

    #print('Hello')
