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
CAT     = KC.LCTL(KC.ALT(KC.DEL))
MUTET   = KC.LCTL(KC.LSFT(KC.M))
VIDT    = KC.LCTL(KC.LSFT(KC.O))
HANDT   = KC.LCTL(KC.LSFT(KC.K))
SCCAP   = KC.LCTL(KC.PSCR)


# Strings
CURPASS     = send_string("CURPASS")
HANGMANL    = send_string("HANGMANL")
HANGMANU    = send_string("HANGMANU")
UID         = send_string("UID")
OWSH        = send_string("OWSH")
OWTT        = send_string("OWTT")
OWTTU       = send_string("OWTTU")
WKPAUG      = send_string("WKPAUG")
TEAMCT      = send_string("TEAMCT")
MYEMAIL     = send_string("MYEMAIL")
RABSC       = send_string("RABSC")
EPPS        = send_string("EPPS")
PKH         = send_string("PKH")
OLDPASS     = send_string("OLDPASS")
OLDPASS2    = send_string("OLDPASS2")

# Keymaps
keyboard.keymap = [
    [   # 0.QWY - Qwerty/Base layer
        KC.ESC,     KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,               KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,       KC.MINS,
        RSEL,       KC.A,       KC.S,       KC.D,       KC.F,       KC.G,               KC.H,       KC.J,       KC.K,       KC.L,       KC.SCLN,    KC.QUOT,
        SHCAP,      KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,               KC.N,       KC.M,       KC.COMM,    KC.DOT,     KC.SLSH,    KC.BSLS,
                                KC.F2,      KC.F5,                                                              KC.DEL,     KC.MUTE,
        LWRL,       SHSPC,      KC.BSPC,    KC.LGUI,    KC.LCTL,    KC.LALT,            CAT,        KC.QUOT,    KC.MINS,    KC.ENT,     RSER,       ADJ
    ],
    [   # 1.CDH - Colemark DH/Base-ish layer
        KC.ESC,     KC.Q,       KC.W,       KC.F,       KC.P,       KC.B,               KC.J,       KC.L,       KC.U,       KC.Y,       KC.SCLN,    KC.MINS,
        RSEL,       KC.A,       KC.R,       KC.S,       KC.T,       KC.G,               KC.M,       KC.N,       KC.E,       KC.I,       KC.O,       KC.QUOT,
        SHCAP,      KC.Z,       KC.X,       KC.C,       KC.D,       KC.V,               KC.H,       KC.K,       KC.COMM,    KC.DOT,     KC.SLSH,    KC.BSLS,
                                KC.F2,      KC.F5,                                                              KC.DEL,     KC.MUTE,
        LWRL,       SHSPC,      KC.BSPC,    KC.LGUI,    KC.LCTL,    KC.LALT,            CAT,        KC.QUOT,    KC.MINS,    KC.ENT,     RSER,       ADJ
    ],
    [   # 2.LWR - Numbers and symbols
        KC.TILD,    KC.EXLM,    KC.AT,      KC.HASH,    KC.DLR,     KC.PERC,            KC.CIRC,    KC.AMPR,    KC.ASTR,    KC.LPRN,    KC.RPRN,    KC.PMNS,
        KC.GRV,     KC.P1,      KC.P2,      KC.P3,      KC.P4,      KC.P5,              KC.P6,      KC.P7,      KC.P8,      KC.P9,      KC.P0,      KC.PPLS,
        KC.F5,      KC.TILD,    KC.GRV,     KC.PIPE,    KC.LCBR,    KC.LBRC,            KC.RBRC,    KC.RCBR,    KC.MINS,    KC.EQL,     KC.PPLS,    KC.EQL,
                                KC.LCBR,    KC.LBRC,                                                            KC.DEL,     KC.MPLY,
        KC.TRNS,    SHSPC,      KC.BSPC,    KC.LGUI,    KC.LCTL,    KC.LALT,            CAT,        KC.QUOT,    KC.MINS,    KC.ENT,     RSER,       ADJ
    ],
    [   # 3.RSE - Direction and CTRL based hot keys
        KC.TRNS,    ALTF4,      KC.LCTL,    SCCAP,      CTSH,       KC.LSFT,            CTY,        KC.HOME,    KC.END,     KC.PGUP,    KC.PGDN,    KC.TRNS,
        KC.TRNS,    CTA,        CTS,        CTX,        CTC,        CTV,                KC.TRNS,    KC.LEFT,    KC.DOWN,    KC.UP,      KC.RGHT,    KC.TRNS,
        KC.TRNS,    CTZ,        CTI,        CTB,        CTF,        CTENT,              KC.TRNS,    KC.TRNS,    GCRGHT,     GCLEFT,     KC.TRNS,    KC.TRNS,
                                KC.TRNS,    SAI,                                                                GSRGHT,     GSLEFT,
        CTTAB,      MUTET,      VIDT,       KC.PGUP,    KC.PGDN,    HANDT,              KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS
    ],
    [   # 4.ADJ - Text combos and function keys
        KC.TRNS,    KC.F1,      KC.F2,      KC.F3,      KC.F4,      KC.F5,              KC.F6,      KC.F7,      KC.F8,      KC.F9,      KC.F10,     KC.TRNS,
        KC.TAB,     KC.TRNS,    EPPS,       OLDPASS2,   OLDPASS,    WKPAUG,             PKH,        KC.TRNS,    KC.TRNS,    KC.F11,     KC.F12,     KC.TRNS,
        KC.TRNS,    KC.TRNS,    OWTTU,      OWSH,       OWTT,       TEAMCT,             MYEMAIL,    UID,        CURPASS,    KC.TRNS,    KC.TRNS,    KC.TRNS,
                                QWY,        KC.RESET,                                                           KC.RESET,   CDH,
        CURPASS,    UID,        MYEMAIL,    RABSC,      HANGMANU,   HANGMANL,           KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS
    ],
]
print('Hello')
