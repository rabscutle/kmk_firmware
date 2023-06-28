import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.quickpin.pro_micro.avr_promicro import translate as avr
from kmk.quickpin.pro_micro.boardsource_blok import pinout as pins
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    row_pins = (
        pins[avr['GP04']],
        pins[avr['GP05']],
        pins[avr['GP06']],
        pins[avr['GP07']],
        pins[avr['GP08']],
        pins[avr['GP09']]
    )
    col_pins = (
        pins[avr['GP26']],
        pins[avr['GP22']],
        pins[avr['GP20']],
        pins[avr['GP23']],
        pins[avr['GP21']]
    )
    diode_orientation = DiodeOrientation.COLUMNS
    data_pin = pins[avr['GP04']]
    # data_pin2 =
    # rgb_pixel_pin = pins[avr['D3']]
    # num_pixels = 12

    # flake8: noqa
    # fmt: off
    coord_mapping = [
        0,  1,  2,  3,  4,  5,            35, 34, 33, 32, 31, 30,
        6,  7,  8,  9,  10, 11,           41, 40, 39, 38, 37, 36,
        12, 13, 14, 15, 16, 17,           47, 46, 45, 44, 43, 42,
                20, 21,                           51, 50,
        24, 25, 26, 27, 28, 29,           59, 58, 57, 56, 55, 54
    ]

