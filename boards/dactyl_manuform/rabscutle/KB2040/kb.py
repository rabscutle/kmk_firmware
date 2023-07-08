import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.scanners.digitalio import MatrixScanner
import digitalio

class MyKeyboard(KMKKeyboard):
    def __init__(self):
        # self.debug_enabled = True
        self.row_pins = (
            board.D5,
            board.D6,
            board.D7,
            board.D8,
            board.D9,
        )
        self.col_pins = (
            board.A1,
            board.A0,
            board.SCK,
            board.MISO,
            board.MOSI,
            board.D10,
        )
        self.diode_orientation = DiodeOrientation.COLUMNS
        self.data_pin = board.TX
        # create and register the scanner
        self.matrix = MatrixScanner(
            cols=self.col_pins,
            rows=self.row_pins,
            diode_orientation=self.diode_orientation,
            pull=digitalio.Pull.DOWN,
            rollover_cols_every_rows=None, # optional
        )
        self.coord_mapping = [
        0,  1,  2,  3,  4,  5,            35, 34, 33, 32, 31, 30,
        6,  7,  8,  9,  10, 11,           41, 40, 39, 38, 37, 36,
        12, 13, 14, 15, 16, 17,           47, 46, 45, 44, 43, 42,
                20, 21,                           51, 50,
        24, 25, 26, 27, 28, 29,           59, 58, 57, 56, 55, 54
        ]
