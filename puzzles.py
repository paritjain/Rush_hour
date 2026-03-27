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

def _puzzler_easy() -> GameState:
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
