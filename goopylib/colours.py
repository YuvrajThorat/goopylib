from goopylib.util import GraphicsError
from random import randint as randomrandint

# Defining Custom  & colour Functions

class Colour:
    def __init_subclass__(cls, **kwargs):
        cls.colour = None
        cls.string = "colour"

        cls.red = 0
        cls.green = 0
        cls.blue = 0

    def __str__(self):
        return self.colour

    def __repr__(self):
        return self.string

    def __abs__(self):
        c_value = (self.red + self.green + self.blue) / 3
        return ColourRGB(c_value, c_value, c_value)

    def __sub__(self, other):
        try:
            red = self.red - other.red
            green = self.green - other.green
            blue = self.blue - other.blue
        except AttributeError:
            red = self.red - other
            green = self.green - other
            blue = self.blue - other

        return ColourRGB(max([red, 0]), max([green, 0]), max([blue, 0]))

    def __add__(self, other):
        try:
            red = self.red + other.red
            green = self.green + other.green
            blue = self.blue + other.blue
        except AttributeError:
            red = self.red + other
            green = self.green + other
            blue = self.blue + other

        return ColourRGB(min([red, 255]), min([green, 255]), min([blue, 255]))

    def __mul__(self, other):
        try:
            red = self.red * other.red
            green = self.green * other.green
            blue = self.blue * other.blue
        except AttributeError:
            red = self.red * other
            green = self.green * other
            blue = self.blue * other

        return ColourRGB(red, green, blue)

    def __floordiv__(self, other):
        try:
            red = self.red // other.red
            green = self.green // other.green
            blue = self.blue // other.blue
        except AttributeError:
            red = self.red // other
            green = self.green // other
            blue = self.blue // other

        return ColourRGB(red, green, blue)

    def __truediv__(self, other):
        return self // other

    def __mod__(self, other):
        try:
            red = self.red % other.red
            green = self.green % other.green
            blue = self.blue % other.blue
        except AttributeError:
            red = self.red % other
            green = self.green % other
            blue = self.blue % other

        return ColourRGB(red, green, blue)
    
    def __pow__(self, power, modulo=None):
        try:
            red = self.red ** power.red
            green = self.green ** power.green
            blue = self.blue ** power.blue
        except AttributeError:
            red = self.red ** power
            green = self.green ** power
            blue = self.blue ** power

        return ColourRGB(red, green, blue) % modulo

    def __neg__(self):
        return ColourRGB(255 - self.red, 255 - self.green, 255 - self.blue)

    def __pos__(self):
        return ColourRGB(self.red, self.green, self.blue)

    def __lshift__(self, other):
        try:
            red = self.red << other.red
            green = self.green << other.green
            blue = self.blue << other.blue
        except AttributeError:
            red, green, blue = self.red, self.green, self.blue
            for _ in range(other):
                red, green, blue = green, blue, red

        return ColourRGB(red, green, blue)

    def __rshift__(self, other):
        try:
            red = self.red >> other.red
            green = self.green >> other.green
            blue = self.blue >> other.blue
        except AttributeError:
            red, green, blue = self.red, self.green, self.blue
            for _ in range(other):
                red, green, blue = blue, red, green

        return ColourRGB(red, green, blue)

    def __xor__(self, other):
        try:
            red = self.red ^ other.red
            green = self.green ^ other.green
            blue = self.blue ^ other.blue
        except AttributeError:
            red = self.red ^ other
            green = self.green ^ other
            blue = self.blue ^ other

        return ColourRGB(red, green, blue)

    def __invert__(self):
        return -self

    def __and__(self, other):
        try:
            red = self.red & other.red
            green = self.green & other.green
            blue = self.blue & other.blue
        except AttributeError:
            red = self.red & other
            green = self.green & other
            blue = self.blue & other

        return ColourRGB(red, green, blue)
    
    def __or__(self, other):
        try:
            red = self.red | other.red
            green = self.green | other.green
            blue = self.blue | other.blue
        except AttributeError:
            red = self.red | other
            green = self.green | other
            blue = self.blue | other

        return ColourRGB(red, green, blue)

    def __bool__(self):
        if self.colour != "#000000":
            return True
        return False

    def __bytes__(self):
        return bytes(self.colour)

    def __contains__(self, item):
        if self.red == item or self.blue == item or self.green == item:
            return True
        elif item in self.colour[1:3] or item in self.colour[3:5] or item in self.colour[5:7]:
            return True
        elif isinstance(item, Colour):
            return item == self
        return False

    def __copy__(self):
        return ColourRGB(self.red, self.green, self.blue)

    def __lt__(self, other):
        return self.red + self.green + self.blue < other.red + other.green + other.blue

    def __le__(self, other):
        return self.red + self.green + self.blue <= other.red + other.green + other.blue

    def __gt__(self, other):
        return self.red + self.green + self.blue > other.red + other.green + other.blue

    def __ge__(self, other):
        return self.red + self.green + self.blue >= other.red + other.green + other.blue

    def __eq__(self, other):
        return self.colour == other.colour

    def __ne__(self, other):
        return self.colour != other.colour

    def rgb(self):
        return f"rgb {self.red}, {self.blue}, {self.green}"


class ColourRGB(Colour):
    def __init__(self, r, g, b):
        if not (isinstance(r, int) and isinstance(g, int) and isinstance(b, int)):
            raise GraphicsError("\n\nRGB values must be integers!")
        if not (256 > r > -1 and 256 > g > -1 and 256 > b > -1):
            raise GraphicsError(
                "\n\nRGB values must be between 0 & 255 (included), right now {}, {}, {}".format(r, g, b))
        self.colour = "#%02x%02x%02x" % (r, g, b)
        self.string = f"rgb {r}, {g}, {b}"

        self.red = +r
        self.green = +g
        self.blue = +b


class ColourHex(Colour):
    def __init__(self, colour):
        if not isinstance(colour, str):
            raise GraphicsError("\n\nHex value must be a string in format: #rrggbb")
        if not 6 <= len(colour) <= 7:
            raise GraphicsError("\n\nThe length of the hex colour string must be 6: 'rrggbb'")

        if len(colour) == 6:
            self.colour = f"#{self.colour}"
        self.colour = colour
        self.string = self.colour

        colour = colour[1:]
        rgb = [int(colour[i:i+2], 16) for i in (0, 2, 4)]
        self.red = rgb[0]
        self.green = rgb[1]
        self.blue = rgb[2]


class ColourCMYK(Colour):
    def __init__(self, c, y, m, k):
        if not (isinstance(c, int) and isinstance(y, int) and isinstance(m, int) and isinstance(k, int)):
            raise GraphicsError("\n\nCMYK values must be integers!")
        if not (101 > c > -1 and 101 > y > -1 and 101 > m > -1 and 101 > k > -1):
            raise GraphicsError(f"\n\nCMYK values must be between 0 & 100 (included), right now {c}, {m}, {y}, {k}")

        r = 255 * (1 - (c + k) // 100)
        g = 255 * (1 - (m + k) // 100)
        b = 255 * (1 - (y + k) // 100)

        self.colour = "#%02x%02x%02x" % (r, g, b)
        self.string = f"cmyk {c}, {m}, {y}, {k}"

        self.red = r
        self.green = g
        self.blue = b


def RandomColourRGB(red=None, green=None, blue=None):
    if red is None:
        red = randomrandint(0, 255)
    if green is None:
        green = randomrandint(0, 255)
    if blue is None:
        blue = randomrandint(0, 255)
    return ColourRGB(red, green, blue)

def RandomColourCMYK(c=None, m=None, y=None, k=None):
    if c is None:
        c = randomrandint(0, 100)
    if m is None:
        m = randomrandint(0, 100)
    if y is None:
        y = randomrandint(0, 100)
    if k is None:
        k = randomrandint(0, 100)
    return ColourCMYK(c, m, y, k)

def RandomColourHex(red=None, green=None, blue=None):
    if red is None:
        red = randomrandint(0, 255)
    else:
        red = int(red, 16)
    if green is None:
        green = randomrandint(0, 255)
    else:
        green = int(green, 16)
    if blue is None:
        blue = randomrandint(0, 255)
    else:
        blue = int(blue, 16)
    return ColourHex("#%02x%02x%02x" % (red, green, blue))

def RandomGreyscale(start=0, end=255):
    grey = randomrandint(start, end)
    return ColourRGB(grey, grey, grey)


def ColourGradient(colour_start=ColourRGB(255, 255, 255), colour_end=ColourRGB(0, 0, 0), divisions=10):
    red_dist = colour_end.red - colour_start.red
    green_dist = colour_end.green - colour_start.green
    blue_dist = colour_end.blue - colour_start.blue

    cur_red, cur_green, cur_blue = colour_start.red, colour_start.green, colour_start.blue

    gradient = []
    for i in range(divisions - 1):
        gradient.append(ColourRGB(max([0, cur_red]), max([cur_green, 0]), max([cur_blue, 0])))
        cur_red = colour_start.red + i * red_dist // divisions
        cur_green = colour_start.green + i * green_dist // divisions
        cur_blue = colour_start.blue + i * blue_dist // divisions

    gradient.append(colour_end)
    return gradient

def ColourGradient2D(colour_start1=ColourRGB(0, 0, 0), colour_end1=ColourRGB(255, 0, 0),
                     colour_start2=ColourRGB(255, 255, 255), colour_end2=ColourRGB(0, 255, 0),
                     divisions_x=10, divisions_y=10):

    top_gradient = ColourGradient(colour_start1, colour_end1, divisions=divisions_x)
    bottom_gradient = ColourGradient(colour_start2, colour_end2, divisions=divisions_x)

    cur_red, cur_green, cur_blue = colour_start1.red, colour_start1.green, colour_start1.blue

    gradient = [[None for _ in range(divisions_y)] for _ in range(divisions_x)]

    for col in range(divisions_x):
        gradient[col][0] = top_gradient[col]
        gradient[col][-1] = bottom_gradient[col]

    for col in range(0, len(gradient)):
        gradient[col] = ColourGradient(gradient[col][0], gradient[col][-1], divisions_y)

    return gradient


# The Blacks, Greys, and Whites
BLACK = ColourRGB(0, 0, 0)
DARKEST_GREY = ColourRGB(30, 30, 30)
DARKER_GREY = ColourRGB(40, 40, 40)
DARK_GREY = ColourRGB(45, 45, 45)

DARKISH_GREY = ColourRGB(60, 60, 60)
GREY = ColourRGB(100, 100, 100)
LIGHTISH_GREY = ColourRGB(130, 130, 130)
LIGHT_GREY = ColourRGB(160, 160, 160)
LIGHTER_GREY = ColourRGB(187, 187, 187)
LIGHTEST_GREY = ColourRGB(210, 210, 210)

DARK_WHITE = ColourRGB(240, 240, 240)
WHITE = ColourRGB(255, 255, 255)

# Blue-Greys
DARKEST_BLUE_GREY = ColourRGB(30, 32, 34)
DARKER_BLUE_GREY = ColourRGB(40, 42, 44)
DARK_BLUE_GREY = ColourRGB(49, 51, 53)

DARKISH_BLUE_GREY = ColourRGB(55, 57, 59)
BLUE_GREY = ColourRGB(63, 75, 86)
LIGHTISH_BLUE_GREY = ColourRGB(83, 95, 106)
LIGHT_BLUE_GREY = ColourRGB(103, 115, 126)
LIGHTER_BLUE_GREY = ColourRGB(133, 145, 156)
LIGHTEST_BLUE_GREY = ColourRGB(173, 185, 196)

# Warm Colours
DARKEST_RED = ColourRGB(48, 11, 8)
DARKER_RED = ColourRGB(64, 13, 9)
DARK_RED = ColourRGB(99, 18, 12)

DARKISH_RED = ColourRGB(143, 23, 12)
RED = ColourRGB(194, 22, 6)
LIGHTISH_RED = ColourRGB(224, 66, 52)
LIGHT_RED = ColourRGB(255, 94, 79)

PINK = ColourRGB(255, 122, 110)
LIGHTISH_PINK = ColourRGB(255, 133, 122)
LIGHT_PINK = ColourRGB(255, 161, 153)
LIGHTER_PINK = ColourRGB(255, 194, 189)
LIGHTEST_PINK = ColourRGB(255, 224, 222)

ABSOLUTE_RED = ColourRGB(255, 0, 0)


# Orange & Brown Shades from: https://graf1x.com/shades-of-orange-color-palette/
# ORANGES
MELON_ORANGE = ColourRGB(247, 152, 98)
SALAMANDER_ORANGE = ColourRGB(240, 94, 35)
SANDSTONE_ORANGE = ColourRGB(215, 144, 44)
GINGER_ORANGE = ColourRGB(190, 85, 4)
SQUASH_ORANGE = ColourRGB(203, 92, 13)

ORANGE = ColourRGB(252, 102, 0)
ROYAL_ORANGE = ColourRGB(249, 129, 42)
TIGER_ORANGE = ColourRGB(253, 106, 2)
APRICOT_ORANGE = ColourRGB(239, 130, 13)
OCHRE_ORANGE = ColourRGB(204, 119, 34)
FIRE_ORANGE = ColourRGB(253, 165, 15)
CARROT_ORANGE = ColourRGB(239, 114, 21)
PUMPKIN_ORANGE = ColourRGB(255, 116, 23)
HONEY_ORANGE = ColourRGB(235, 150, 5)

# BROWNS

DARK_AMBER_BROWN = ColourRGB(136, 48, 0)
BRONZE_BROWN = ColourRGB(177, 86, 15)
CLAY_BROWN = ColourRGB(129, 63, 11)
BURNT_BROWN = ColourRGB(150, 64, 0)

LIGHTEST_BROWN = ColourRGB(168, 145, 113)
LIGHTER_BROWN = ColourRGB(145, 119, 83)
LIGHT_BROWN = ColourRGB(122, 91, 47)
BROWN = ColourRGB(156, 91, 0)
DARKER_BROWN = ColourRGB(94, 62, 18)
DARKEST_BROWN = ColourRGB(64, 38, 3)

# YELLOWS
# From https://graf1x.com/shades-of-yellow-color-palette-chart/

GOLD = ColourRGB(249, 166, 2)
GOLDENROD_YELLOW = ColourRGB(218, 165, 32)
YELLOW = ColourRGB(252, 226, 5)

AMBER_YELLOW = ColourRGB(255, 191, 0)
ROYAL_YELLOW = ColourRGB(250, 218, 94)
MUSTARD_YELLOW = ColourRGB(254, 220, 86)
MELLOW_YELLOW = ColourRGB(248, 222, 126)
FLAX_YELLOW = ColourRGB(238, 220, 130)
CREAM_YELLOW = ColourRGB(255, 253, 208)
CHROME_YELLOW = ColourRGB(255, 204, 0)
TROMBONE_YELLOW = ColourRGB(210, 181, 91)

ABSOLUTE_YELLOW = ColourRGB(255, 255, 0)

# Greens
DARK_GREEN = ColourRGB(0, 104, 60)
OLIVE_GREEN = ColourRGB(0, 100, 5)
GREEN = ColourRGB(0, 123, 45)
LIGHT_GREEN = ColourRGB(51, 187, 15)

ABSOLUTE_GREEN = ColourRGB(0, 255, 0)

# Blues
DARKEST_NAVY_BLUE = ColourRGB(20, 27, 34)
DARKER_NAVY_BLUE = ColourRGB(30, 37, 44)
DARK_NAVY_BLUE = ColourRGB(38, 45, 56)
NAVY_BLUE = ColourRGB(45, 57, 68)
BLUE = ColourRGB(0, 153, 255)
CYAN = None

TURQUOISE = ColourRGB(79, 227, 194)

ABSOLUTE_BLUE = ColourRGB(0, 0, 255)

# Purples & Pinks
DARK_PURPLE = None
PURPLE = None
LIGHT_PURPLE = None
