from kb import MyKeyboard
import board

from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC
from kmk.modules.holdtap import HoldTap
from kmk.modules.layers import Layers
from kmk.handlers.sequences import send_string
from kmk.modules.split import Split, SplitSide, SplitType

keyboard = MyKeyboard()

keyboard.modules.append(Layers())
keyboard.modules.append(HoldTap())
keyboard.extensions.append(MediaKeys())


split = Split(
    #split_type=SplitType.UART,  # Defaults to UART
    split_side=SplitSide.LEFT,  # Sets if this is to SplitSide.LEFT or SplitSide.RIGHT, or use EE hands    
    split_flip=True,  # If both halves are the same, but flipped, set this True
    #split_target_left=True,  # Assumes that left will be the one on USB. Set to False if it will be the right
    #uart_interval=20,  # Sets the uarts delay. Lower numbers draw more power
    data_pin=board.TX,  # The primary data pin to talk to the secondary device with
    data_pin2=board.RX,  # Second uart pin to allow 2 way communication
    use_pio=True,  # Use RP2040 PIO implementation of UART. Required if you want to use other pins than RX/TX
    uart_flip=True,  # Reverses the RX and TX pins if both are provided
)

keyboard.modules.append(split)

# Layer Keys
QWY  = KC.DF(0)
CDH  = KC.DF(1)
LWR  = KC.MO(2)
RSE  = KC.MO(3)
RSE  = KC.MO(3)
ADJ  = KC.MO(4)
LWRL = KC.LT(2, KC.SPC, prefer_hold=True, tap_interrupted=False, tap_time=250)
LWRR = KC.LT(2, KC.SPC, prefer_hold=True, tap_interrupted=False, tap_time=250)
RSER = KC.LT(3, KC.SPC, prefer_hold=True, tap_interrupted=False, tap_time=250)
RSEL = KC.LT(3, KC.TAB, prefer_hold=True, tap_interrupted=False, tap_time=250)

# Hold Tap Keys
SHCAP = KC.HT(KC.CAPS,KC.LSFT)
SHSPC = KC.HT(KC.SPC, KC.LSFT)

# CTL Hotkeys
ALTF4  = KC.LALT(KC.F4)
CTA   = KC.LCTL(KC.A)
CTS   = KC.LCTL(KC.S)
CTX   = KC.LCTL(KC.X)
CTC   = KC.LCTL(KC.C)
CTV   = KC.LCTL(KC.V)
CTZ   = KC.LCTL(KC.Z)
CTI   = KC.LCTL(KC.I)
CTB   = KC.LCTL(KC.B)
CTF   = KC.LCTL(KC.F)
CTENT = KC.LCTL(KC.ENT)
CTY   = KC.LCTL(KC.Y)
SAI   = KC.LSFT(KC.LALT(KC.I))
CTSH  = KC.LCTL(KC.LSFT)
CTTAB   = KC.LCTL(KC.TAB)
GCLEFT  = KC.LGUI(KC.LCTL(KC.LEFT))
GCRGHT  = KC.LGUI(KC.LCTL(KC.RGHT))
GSLEFT  = KC.LGUI(KC.LSFT(KC.LEFT))
GSRGHT  = KC.LGUI(KC.LSFT(KC.RGHT))
CAT     = KC.LCTL(KC.LALT(KC.DEL))
MUTET   = KC.LCTL(KC.LSFT(KC.M))
VIDT    = KC.LCTL(KC.LSFT(KC.O))
HANDT   = KC.LCTL(KC.LSFT(KC.K))
SCCAP   = KC.LCTL(KC.PSCR)

# Strings
STR1 = send_string("A test string")
STR2 = send_string("Another test string")

# Keymaps
keyboard.keymap = [
    [   # 0.QWY - Qwerty/Base layer
        KC.ESC,     KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,               KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,       KC.MINS,
        RSEL,       KC.A,       KC.S,       KC.D,       KC.F,       KC.G,               KC.H,       KC.J,       KC.K,       KC.L,       KC.SCLN,    KC.QUOT,
        SHCAP,      KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,               KC.N,       KC.M,       KC.COMM,    KC.DOT,     KC.SLSH,    KC.BSLS,
                                KC.F2,      KC.F5,                                                              KC.DEL,     KC.MUTE,
        LWRL,       SHSPC,      KC.BSPC,    KC.LGUI,    KC.LALT,    KC.LCTL,            KC.QUOT,    CAT,        KC.MINS,    KC.ENT,     RSER,       ADJ
    ],
    [   # 1.CDH - Colemark DH/Base-ish layer
        KC.ESC,     KC.Q,       KC.W,       KC.F,       KC.P,       KC.B,               KC.J,       KC.L,       KC.U,       KC.Y,       KC.SCLN,    KC.MINS,
        RSEL,       KC.A,       KC.R,       KC.S,       KC.T,       KC.G,               KC.M,       KC.N,       KC.E,       KC.I,       KC.O,       KC.QUOT,
        SHCAP,      KC.Z,       KC.X,       KC.C,       KC.D,       KC.V,               KC.H,       KC.K,       KC.COMM,    KC.DOT,     KC.SLSH,    KC.BSLS,
                                KC.F2,      KC.F5,                                                              KC.DEL,     KC.MUTE,
        LWRL,       SHSPC,      KC.BSPC,    KC.LGUI,    KC.LALT,    KC.LCTL,            KC.QUOT,    CAT,        KC.MINS,    KC.ENT,     RSER,       ADJ
    ],
    [   # 2.LWR - Numbers and symbols
        KC.TILD,    KC.EXLM,    KC.AT,      KC.HASH,    KC.DLR,     KC.PERC,            KC.CIRC,    KC.AMPR,    KC.ASTR,    KC.LPRN,    KC.RPRN,    KC.PMNS,
        KC.GRV,     KC.P1,      KC.P2,      KC.P3,      KC.P4,      KC.P5,              KC.P6,      KC.P7,      KC.P8,      KC.P9,      KC.P0,      KC.PPLS,
        KC.F5,      KC.TILD,    KC.GRV,     KC.PIPE,    KC.LCBR,    KC.LBRC,            KC.RBRC,    KC.RCBR,    KC.MINS,    KC.EQL,     KC.PPLS,    KC.EQL,
                                KC.LCBR,    KC.LBRC,                                                            KC.DEL,     KC.MPLY,
        KC.TRNS,    SHSPC,      KC.BSPC,    KC.LGUI,    KC.LALT,    KC.LCTL,            KC.QUOT,    CAT,        KC.MINS,    KC.ENT,     RSER,       ADJ
    ],
    [   # 3.RSE - Direction and CTRL based hot keys
        KC.TRNS,    ALTF4,      KC.LCTL,    SCCAP,      CTSH,       KC.LSFT,            CTY,        KC.HOME,    KC.END,     KC.PGUP,    KC.PGDN,    KC.TRNS,
        KC.TRNS,    CTA,        CTS,        CTX,        CTC,        CTV,                KC.TRNS,    KC.LEFT,    KC.DOWN,    KC.UP,      KC.RGHT,    KC.TRNS,
        KC.TRNS,    CTZ,        CTI,        CTB,        CTF,        CTENT,              KC.TRNS,    KC.TRNS,    GCRGHT,     GCLEFT,     KC.TRNS,    KC.TRNS,
                                KC.TRNS,    SAI,                                                                GSRGHT,     GSLEFT,
        CTTAB,      MUTET,      VIDT,       KC.PGUP,    HANDT,      KC.PGDN,            KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS
    ],
    [   # 4.ADJ - Text combos and function keys
        KC.TRNS,    KC.F1,      KC.F2,      KC.F3,      KC.F4,      KC.F5,              KC.F6,      KC.F7,      KC.F8,      KC.F9,      KC.F10,     KC.TRNS,
        KC.TAB,     KC.TRNS,    STR1,       STR2,       STR1,       STR2,               STR2,       KC.TRNS,    KC.TRNS,    KC.F11,     KC.F12,     KC.TRNS,
        KC.TRNS,    KC.TRNS,    STR2,       STR1,       STR2,       STR1,               STR1,       STR2,       STR1,       KC.TRNS,    KC.TRNS,    KC.TRNS,
                                QWY,        KC.RESET,                                                           KC.RESET,   CDH,
        STR1,       STR2,       STR1,       STR2,        STR1,      STR2,               KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS
    ],
]

if __name__ == '__main__':
    keyboard.go()
