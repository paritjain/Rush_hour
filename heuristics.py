# Heuristic 1 – Blocking Cars Count
def h_blocking_cars(state) -> int:
    target    = state.cars[TARGET_CAR]
    grid      = state.get_grid()
    blockers  = set()
  
   front_col = target.col + target.length
    for col in range(front_col, BOARD_SIZE):
        cell = grid[target.row][col]
        if cell != '.':
            blockers.add(cell)

    return len(blockers)

# Heuristic 2 – Blocking Cars + Stuck Blockers
def h_advanced(state) -> int:
    target    = state.cars[TARGET_CAR]
    grid      = state.get_grid()
    car_dict  = state.cars
    blockers  = set()
