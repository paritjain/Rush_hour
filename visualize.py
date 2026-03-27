# Try importing pygame
try:
    import pygame
    PYGAME_AVAILABLE = True
except ImportError:
    PYGAME_AVAILABLE = False

# Colour palette (car_id → RGB)

# Maps each car ID to an RGB colour used in visualization.
CAR_COLOURS = {
    'X': (210,  55,  55),   # Red   <- always the target
    'A': ( 65, 130, 190),   # Blue
    'B': ( 34, 150,  60),   # Green
    'C': (230, 145,  20),   # Orange
    'D': (140,  50, 210),   # Purple
    'E': (200, 190,  10),   # Yellow
    'F': ( 20, 185, 195),   # Teal
    'G': (220,  90, 160),   # Pink
}

# Layout constants
CELL       = 90          # pixels per grid cell
PAD        = 50          # board padding
INFO_W     = 270         # width of info panel on the right
BOARD_PX   = 6 * CELL    # 540 px
WIN_W      = BOARD_PX + 2 * PAD + INFO_W
WIN_H      = BOARD_PX + 2 * PAD

BG         = (235, 235, 220)
GRID_LINE  = ( 90,  90,  90)
BORDER     = ( 30,  30,  30)
TEXT_COL   = ( 20,  20,  20)
EXIT_COL   = (210,  55,  55)
