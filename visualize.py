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


# DRAWING HEPLERS

def _car_color(car_id: str):
    return CAR_COLOURS.get(car_id, (160, 160, 160))

def _draw_board(screen, state, font_big, font_small, info_lines: list):
    """Render one frame: board + cars + info panel."""
    screen.fill(BG)

    ox = PAD   # board origin x
    oy = PAD   # board origin y

    # GRID CELLS
    for r in range(6):
        for c in range(6):
            rect = pygame.Rect(ox + c * CELL, oy + r * CELL, CELL, CELL)
            pygame.draw.rect(screen, (215, 215, 200), rect)
            pygame.draw.rect(screen, GRID_LINE, rect, 1)

    # BOARD BOIRDERS

    pygame.draw.rect(screen, BORDER,
                     pygame.Rect(ox, oy, BOARD_PX, BOARD_PX), 3)

    # EXIT ARROW

    ax = ox + BOARD_PX + 4
    ay = oy + 2 * CELL + CELL // 2
    pygame.draw.polygon(screen, EXIT_COL, [
        (ax,      ay - 14),
        (ax + 28, ay),
        (ax,      ay + 14),
    ])

    # CARS

    for car in state.cars.values():
        cells  = car.cells()
        min_r  = min(r for r, _ in cells)
        min_c  = min(c for _, c in cells)
        max_r  = max(r for r, _ in cells)
        max_c  = max(c for _, c in cells)

        car_rect = pygame.Rect(
            ox + min_c * CELL + 5,
            oy + min_r * CELL + 5,
            (max_c - min_c + 1) * CELL - 10,
            (max_r - min_r + 1) * CELL - 10,
        )
        colour = _car_color(car.car_id)

    # CAR BODY

    pygame.draw.rect(screen, colour,  car_rect, border_radius=10)

    # CAR BORDER

    dark = tuple(max(0, v - 60) for v in colour)
    pygame.draw.rect(screen, dark,    car_rect, 2, border_radius=10)

    # CAR LABEL

    label = font_big.render(car.car_id, True, (255, 255, 255))
    lx = car_rect.centerx - label.get_width()  // 2
    ly = car_rect.centery - label.get_height() // 2
    screen.blit(label, (lx, ly))

    # INFO PANEL

    ix = ox + BOARD_PX + 45
    iy = oy
    for i, line in enumerate(info_lines):
        colour = EXIT_COL if line.startswith('★') else TEXT_COL
        surf = font_small.render(line, True, colour)
        screen.blit(surf, (ix, iy + i * 26))

    pygame.display.flip()
    
