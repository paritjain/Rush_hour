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

# Public API

def show_solution(initial_state, solution, algo_name: str, stats: dict):
    """
    Open a window showing the solution step-by-step.

    Controls
    --------
    →>   next step
    <-    previous step
    SPACE toggle auto-play
    Q     quit
    """
    if not PYGAME_AVAILABLE:
        _text_fallback(initial_state, solution, algo_name, stats)
        return

    pygame.init()
    screen     = pygame.display.set_mode((WIN_W, WIN_H))
    pygame.display.set_caption(f'Rush Hour  –  {algo_name}')
    font_big   = pygame.font.SysFont('monospace', 30, bold=True)
    font_small = pygame.font.SysFont('monospace', 17)
    clock      = pygame.time.Clock()

    # Build a flat list of (action_label, state) for every step
    steps = [('Start', initial_state)]
    if solution:
        for (car_id, direction), state in solution:
            steps.append((f'Move {car_id} {direction}', state))

    idx        = 0
    auto_play  = False
    auto_ms    = 0

    def info(i):
        solved = '★ SOLVED!' if steps[i][1].is_goal() else ''
        return [
            f'Algorithm:',
            f'  {algo_name}',
            '',
            f'Nodes explored:',
            f'  {stats["nodes_explored"]}',
            '',
            f'Solution length:',
            f'  {stats["solution_length"]} moves',
            '',
            '─' * 18,
            f'Step {i} / {len(steps)-1}',
            f'  {steps[i][0]}',
            solved,
            '',
            'Controls:',
            '  →> next step',
            '  <- prev step',
            '  SPACE auto-play',
            '  Q  quit',
        ]

while True:
# Event Handling
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            return

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_q:
                pygame.quit()
                return

            elif event.key == pygame.K_RIGHT and idx < len(steps) - 1:
                idx += 1

            elif event.key == pygame.K_LEFT and idx > 0:
                idx -= 1

            elif event.key == pygame.K_SPACE:
                auto_play = not auto_play


 
    # Auto-play Logic

    dt = clock.tick(30)

    if auto_play:
        auto_ms += dt

        if auto_ms >= 700:
            auto_ms = 0

            if idx < len(steps) - 1:
                idx += 1
            else:
                auto_play = False


    # Draw Current State
    _, current_state = steps[idx]

    _draw_board(
        screen,
        current_state,
        font_big,
        font_small,
        info(idx)
    )

    pygame.display.flip()

# FALLBACK

def _text_fallback(initial_state, solution, algo_name, stats):
    """
    Print every step of solution on the terminal. """
    printf(f'\n[Visualizer] pygame not found – showing text output instead.')
    print(f'Algorithm : {algo_name}')
    print(f'Nodes : {stats["nodes_explored"]}')
    print(f'Length : {stats["solution_length"]} moves\n')

    print('─ INITIAL BOARD ─')
    initial_state.print_board()

    if solution:
        for i, ((car_id, direction), state) in enumerate(solution, 1):
            input(f'\nStep {i}: Move {car_id} {direction}  (press Enter)')
            state.print_board()
    else:
        print('No Solution was found.')
            
        
