import board
from kmk.bootcfg import bootcfg

bootcfg(
  sense=board.D9, # row
  source=board.A1,  # column
  storage=False,
  usb_id=('KMK Keyboards', 'Dactyl-Manuform a la Rabscutle 2'),
)

print ("booted")