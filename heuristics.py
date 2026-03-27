from game_state import BOARD_SIZE, TARGET_CAR
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
# Step 1 – find direct blockers (same as h1)
front_col = target.col + target.length
    for col in range(front_col, BOARD_SIZE):
        cell = grid[target.row][col]
        if cell != '.':
            blockers.add(cell)

 # Step 2 – check whether each blocker is stuck
 stuck = 0
    for bid in blockers:
        blocker = car_dict[bid]
        if blocker.orientation == 'V':
            can_up   = (blocker.row > 0
                        and grid[blocker.row - 1][blocker.col] == '.')
            can_down = (blocker.row + blocker.length < BOARD_SIZE
                        and grid[blocker.row + blocker.length][blocker.col] == '.')
            if not can_up and not can_down:
                stuck += 1   
    return len(blockers) + stuck

