from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.holdtap import HoldTap
from kmk.modules.layers import Layers
from kmk.modules.split import Split
from kmk.handlers.sequences import send_string

keyboard = KMKKeyboard()

keyboard.modules.append(Layers())
keyboard.modules.append(HoldTap())

split = Split(
    data_pin=keyboard.data_pin
    # data.pin2=
)
keyboard.modules.append(split)

# Layer Keys
QWY   = KC.DF(0)
CDH   = KC.DF(1)
LWR   = KC.MO(2)
RSE   = KC.MO(3)
ADJ   = KC.MO(4)
L.LWR = KC.LT(2, KC.SPC, prefer_hold=True, tap_interrupted=False, tap_time=250)
R.LWR = KC.LT(2, KC.SPC, prefer_hold=True, tap_interrupted=False, tap_time=250)
R.RSE = KC.LT(3, KC.SPC, prefer_hold=True, tap_interrupted=False, tap_time=250)
L.RSE = KC.LT(3, KC.TAB, prefer_hold=True, tap_interrupted=False, tap_time=250)

# Hold Tap Keys
SH.CAP = KC.HT(KC.CAPS,KC.LSFT)
SH.SPC = KC.HT(KC.SPC, KC.LSFT)

# CTL Hotkeys
A.F4  = KC.LALT(KC.F4)
C.A   = KC.LCTL(KC.A)
C.S   = KC.LCTL(KC.S)
C.X   = KC.LCTL(KC.X)
C.C   = KC.LCTL(KC.C)
C.V   = KC.LCTL(KC.V)
C.Z   = KC.LCTL(KC.Z)
C.I   = KC.LCTL(KC.I)
C.B   = KC.LCTL(KC.B)
C.F   = KC.LCTL(KC.F)
C.ENT = KC.LCTL(KC.ENT)
C.Y   = KC.LCTL(KC.Y)
SA.I  = KC.LSFT(KC.LALT(KC.I))
C.SH  = KC.LCTL(KC.LSFT)
GC.LEFT  = KC.LGUI(KC.LCTL(KC.LEFT))
GC.RGHT  = KC.LGUI(KC.LCTL(KC.RGHT))
GS.LEFT  = KC.LGUI(KC.LSFT(KC.LEFT))
GS.RGHT  = KC.LGUI(KC.LSFT(KC.RGHT))
CAT      = KC.LCTL(KC.ALT(KC.DEL))
MUTE.T   = KC.LCTL(KC.LSFT(KC.M))
VID.T    = KC.LCTL(KC.LSFT(KC.O))
HAND.T   = KC.LCTL(KC.LSFT(KC.K))


# Strings
CURPASS     = send_string("youdontneedAhat#23")
HANGMANL    = send_string("Yo$D0ntN3#d_Hat2bAC0wb0y")
HANGMANU    = send_string("yO$d0NTn3#D_hAT2Bac0WB0Y")
UID         = send_string("s009866")
OWSH        = send_string("0th3RW0rld$")
OWTT        = send_string("0th3RW0rld$ThanTh#s3")
OWTTU       = send_string("0TH3rw0RLD$tHANtH#S3")
WKPAUG      = send_string("we3k8p@ug")
TEAMCT      = send_string("T#AmCT4l1F3")
MYEMAIL     = send_string("patrick.henson@standard.com")
RABSC       = send_string("rabscutle")
EPPS        = send_string("Monday#1")
PKH         = send_string("pkhtexas@yahoo.com")
OLDPASS     = send_string("FuckingSickOfDust#23")
OLDPASS2    = send_string("SpicyPidg30#")

# Keymaps
keyboard.keymap = [
    [   # 0.QWY - Qwerty/Base layer
        KC.ESC,     KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,               KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,       KC.MINS,
        L.RSE,      KC.A,       KC.S,       KC.D,       KC.F,       KC.G,               KC.H,       KC.J,       KC.K,       KC.L,       KC.SCLN,    KC.QUOT,
        SH.CAP,     KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,               KC.N,       KC.M,       KC.COMM,    KC.DOT,     KC.SLSH,    KC.BSLS,
                                KC.F2,      KC.F5,                                                              KC.DEL,     KC.MUTE,
        L.LWR,      SH.SPC,     KC.BSPC,    KC.LGUI,    KC.LCTL,    KC.LALT,            CAT,        KC.QUOT,    KC.MINS,    KC.ENT,     R.RSE,      R.ADJ
    ],
    [   # 1.CDH - Colemark DH/Base-ish layer
        KC.ESC,     KC.Q,       KC.W,       KC.F,       KC.P,       KC.B,               KC.J,       KC.L,       KC.U,       KC.Y,       KC.SCLN,    KC.MINS,
        L.RSE,      KC.A,       KC.R,       KC.S,       KC.T,       KC.G,               KC.M,       KC.N,       KC.E,       KC.I,       KC.O,       KC.QUOT,
        SH.CAP,     KC.Z,       KC.X,       KC.C,       KC.D,       KC.V,               KC.H,       KC.K,       KC.COMM,    KC.DOT,     KC.SLSH,    KC.BSLS,
                                KC.F2,      KC.F5,                                                              KC.DEL,     KC.MUTE,
        L.LWR,      SH.SPC,     KC.BSPC,    KC.LGUI,    KC.LCTL,    KC.LALT,            CAT,        KC.QUOT,    KC.MINS,    KC.ENT,     R.RSE,      R.ADJ
    ],
    [   # 2.LWR - Numbers and symbols
        KC.TILD,    KC.EXLM,    KC.AT,      KC.HASH,    KC.DLR,     KC.PERC,            KC.CIRC,    KC.AMPR,    KC.ASTR,    KC.LPRN,    KC.RPRN,    KC.PMNS,
        KC.GRV,     KC.P1,      KC.P2,      KC.P3,      KC.P4,      KC.P5,              KC.P6,      KC.P7,      KC.P8,      KC.P9,      KC.P0,      KC.PPLS,
        KC.F5,      KC.TILD,    KC.GRV,     KC.PIPE,    KC.LCBR,    KC.LBRC,            KC.RBRC,    KC.RCBR,    KC.MINS,    KC.EQL,     KC.PPLS,    KC.EQL,
                                KC.LCBR,    KC.LBRC,                                                            KC.DEL,     KC.MPLY,
        KC.TRNS,    SH.SPC,     KC.BSPC,    KC.LGUI,    KC.LCTL,    KC.LALT,            CAT,        KC.QUOT,    KC.MINS,    KC.ENT,     R.RSE,      R.ADJ
    ],
    [   # 3.RSE - Direction and CTRL based hot keys
        KC.TRNS,    C.F4,       KC.LCTL,    SC.CAP,     C.SH,       KC.LSFT,            C.Y,        KC.HOME,    KC.END,     KC.PGUP,    KC.PGDN,    KC.TRNS,
        KC.TRNS,    C.A,        C.S,        C.X,        C.C,        C.V,                KC.TRNS,    KC.LEFT,    KC.DOWN,    KC.UP,      KC.RGHT,    KC.TRNS,
        KC.TRNS,    C.Z,        C.I,        C.B,        C.F,        C.ENT,              KC.TRNS,    KC.TRNS,    GC.RGHT,    GC.LEFT,    KC.TRNS,    KC.TRNS,
                                KC.TRNS,    SA.I,                                                               GS.RGHT,    GS.LEFT,
        LCTL(KC.TAB),MUTE.T,    VID.T,      KC.PGUP,    KC.PGDN,    HAND.T,             KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS
    ],
    [   # 4.ADJ - Text combos and function keys
        KC.TRNS,    KC.F1,      KC.F2,      KC.F3,      KC.F4,      KC.F5,              KC.F6,      KC.F7,      KC.F8,      KC.F9,      KC.F10,     KC.TRNS,
        KC.TAB,     KC.TRNS,    EPPS,       OLDPASS2,   OLDPASS,    WKPAUG,             PKH,        KC.TRNS,    KC.TRNS,    KC.F11,     KC.F12,     KC.TRNS,
        KC.TRNS,    KC.TRNS,    OWTTU,      OWSH,       OWTT,       TEAMCT,             MYEMAIL,    UID,        CURPASS,    KC.TRNS,    KC.TRNS,      KC.TRNS,
                                QWY,        KC.RESET,                                                           KC.RESET,   CDH,
        CURPASS,    UID,        MYEMAIL,    RABSC,      HANGMANU,   HANGMANL,           KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS
    ],
]
