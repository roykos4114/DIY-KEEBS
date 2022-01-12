print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation

from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
layers_ext = Layers()


keyboard.col_pins = (board.GP0,board.GP1,board.GP2,board.GP3,board.GP4,board.GP5,board.GP6,board.GP7,board.GP8,board.GP9)
keyboard.row_pins = (board.GP10,board.GP11,board.GP12,board.GP13,board.GP14,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

___________= KC.TRNS
XXXXXXX = KC.NO

LOWER = KC.MO(1)

keyboard.keymap = [
    [KC.N1, KC.N2, KC.N3, KC.N4, KC.N5,                     KC.N6, KC.N7, KC.N8, KC.N9 ,KC.N0,
     KC.Q,    KC.W,    KC.E,    KC.R,   KC.T,                        KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,
     KC.A,    KC.S,    KC.D,    KC.F,   KC.G,                         KC.H,    KC.J,    KC.K,    KC.L,    KC.BSPC,
     KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,                         KC.N,    KC.M,    KC.COMM,    KC.DOT,    KC.ENT,
     KC.LCTL, KC.LWIN, KC.LALT, LOWER, KC.SPC,       KC.RSFT, KC.LEFT, KC.DOWN, KC.UP, KC.RGHT,],
    
    
    [KC.F1, KC.F2, KC.F3, KC.F4, KC.F5,                         KC.F6,  KC.GRV,  KC.SLSH,  KC.MINS , KC.EQL,
     KC.F7, KC.F8,  KC.F9,  KC.F10, KC.F11,                    KC.F12, KC.TILD, KC.LBRC, KC.RBRC, ___________,
     KC.TAB,  ___________,  ___________,  ___________, ___________,                        ___________,  ___________,    KC.SCLN, KC.QUOT, KC.DEL,
     KC.ESC,  ___________,  ___________, ___________,  ___________,                            ___________,  ___________,  ___________,    ___________,  ___________,
     ___________, ___________, ___________, ___________, ___________,                            ___________,  KC.MUTE,   KC.VOLD,  KC.VOLU,    ___________,],


]

if __name__ == '__main__':
    keyboard.go()
