__version__ = "6.10-dev"

from tkinter import Tk as tkTk
from time import time as timetime

# For the list of cursors and thumbnails visit: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/cursors.html
CURSORS = ["arrow", "based_arrow_down", "based_arrow_up", "boat", "bogosity", "bottom_left_corner",
           "bottom_right_corner", "bottom_side", "bottom_tee", "box_spiral", "center_ptr", "circle", "clock",
           "coffee_mug", "cross", "cross_reverse", "crosshair", "diamond_cross", "dot", "dotbox", "double_arrow",
           "draft_large", "draft_small", "draped_box", "exchange", "fleur", "gobbler", "gumpy", "hand1", "hand2",
           "heart", "icon", "iron_cross", "left_ptr", "left_side", "left_tee", "leftbutton", "ll_angle", "lr_angle",
           "man", "middlebutton", "mouse", "pencil", "pirate", "plus", "question_arrow", "right_ptr", "right_side",
           "right_tee", "rightbutton", "rtl_logo", "sailboat", "sb_down_arrow", "sb_h_double_arrow", "sb_left_arrow",
           "sb_right_arrow", "sb_up_arrow", "sb_v_double_arrow", "shuttle", "sizing", "spider", "spraycan", "star",
           "target", "tcross", "top_left_arrow", "top_left_corner", "top_right_corner", "top_side", "top_tee", "trek",
           "ul_angle", "umbrella", "ur_angle", "watch", "xterm", "x_cursor"]
RELIEF = ["flat", "groove", "raised", "ridge", "solid", "sunken"]

##########################################################################
# global variables and functions

_root = tkTk()
_root.withdraw()

_update_lasttime = timetime()
