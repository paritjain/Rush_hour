from game_state import Car, GameState

def get_puzzle(level: int = 1) -> GameState:
  """
  Return a sample puzzle.
    level 1 -> Easy (~5 moves)
    level 2 -> Medium (~6 moves)
    level 3 -> Hard (~8 moves) """
  if level == 1:
    return _puzzle_easy()
  elif level == 2:
    return _puzzle_medium()
  else:
    return _puzzle_hard()

# EASY PUZZLE

def _puzzle_easy() -> GameState:
  """
  Board Layout:  
  
  . . . . . .
  . . . A . .
  X X . A . . -> EXIT
  . . . . . .
  . . . . . .
  . . . . . .
  
  There is just one vertical blocker (A) in the way of the horizontal red car (X).
  Exit is in the same row as the red car (X).
  Solution: Car A up, Red Car X right to exit. """
  return GameState([
    Car('X', 2, 0, 2, 'H'), #Red Car must reach column 4
    Car('A', 1, 3, 2, 'V'), #Car A blocks column 3 in row 2
  ])

# MEDIUM PUZZLE

def _puzzle_medium() -> GameState:
  """
  Board Layout:

  A A . . . .
  . . . B . .
  X X . B . C -> EXIT
  . . . . . C
  . . D D . .
  . . . . . .

  Involves moving Mutiple Cars.
  Solution: Car B moves vertically up, and car C moves vertically up/ down. Path for Red Car to exit is cleared in this manner. """
  return GameState([
        Car('X', 2, 0, 2, 'H'),   # Red car
        Car('A', 0, 0, 2, 'H'),   # Top-left horizontal
        Car('B', 1, 3, 2, 'V'),   # Blocks col 3 in row 2
        Car('C', 2, 5, 2, 'V'),   # Blocks col 5 (the exit column!)
        Car('D', 4, 2, 2, 'H'),   # Bottom horizontal
    ])

# HARD PUZZLE

def _puzzle_hard() -> GameState:
  """
  Board layout:

  . . A . B B
  . . A . . .
  X X A . . . -> EXIT
  . . . C C .
  . D D . . .
  . . . E E .

  Requires 8+ moves to free Red Car.
  Solution: D must move first to let A slide down, which unblocks X. Requires sliding Car D to free up space for car A. """
  return GameState([
        Car('X', 2, 0, 2, 'H'),   # Red Car
        Car('A', 0, 2, 3, 'V'),   # Tall blocker Car in column 2
        Car('B', 0, 4, 2, 'H'),   # Top-right horizontal Car
        Car('C', 3, 3, 2, 'H'),   # Mid-right horizontal Car
        Car('D', 4, 1, 2, 'H'),   # Blocks A from sliding down
        Car('E', 5, 3, 2, 'H'),   # Bottom horizontal Car
    ])
