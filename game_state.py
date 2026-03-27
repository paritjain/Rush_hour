class Car:
    """A single vehicle on the Rush Hour grid."""

    def __init__(self, car_id: str, row: int, col: int, length: int, orientation: str):
     """
        car_id      : single character label ('X', 'A', 'B', …)
        row, col    : top-left corner of the car (0-indexed)
        length      : number of cells occupied (2 or 3)
        orientation : 'H' = horizontal, 'V' = vertical
      """
        self.car_id      = car_id
        self.row         = row
        self.col         = col
        self.length      = length
        self.orientation = orientation 
        
#Helpers
   def cells(self) -> list:
        """Return every (row, col) tuple this car occupies."""
        if self.orientation == 'H':
            return [(self.row, self.col + i) for i in range(self.length)]
        else:
            return [(self.row + i, self.col) for i in range(self.length)]

   def copy(self):
               """Return a deep copy of this car."""
                return Car(self.car_id, self.row, self.col, self.length, self.orientation)

    def __repr__(self):
         return (f"Car('{self.car_id}' " f"r={self.row} c={self.col} " f"{self.orientation}{self.length})")

# GameState
class GameState:
    """Represents the complete board state including all car positions."""
    def __init__(self, cars: list):
        # dictionary keyed by car_id for O(1) lookup
        self.cars = {car.car_id: car for car in cars}
    
   #Goal
   def is_goal(self) -> bool:
        """Return True if the red car reaches the exit column."""
        target = self.cars[TARGET_CAR]
        return target.col + target.length - 1 == BOARD_SIZE - 1

   #Grid Helpers
   def get_grid(self) -> list:
        """Return a BOARD_SIZE × BOARD_SIZE grid with '.' representing empty cells."""
        grid = [['.' for _ in range(BOARD_SIZE)]
                for _ in range(BOARD_SIZE)]
        for car in self.cars.values():
            for r, c in car.cells():
                grid[r][c] = car.car_id
        return grid

    def print_board(self):
        """Print the current board in a readable grid format with exit indicator.."""
        grid = self.get_grid()
        print('+' + '─' * BOARD_SIZE + '+')
        for i, row in enumerate(grid):
            suffix = '>' if i == EXIT_ROW else '│'
            print('│' + ''.join(row) + suffix)
        print('+' + '─' * BOARD_SIZE + '+')

# Move Generation
def get_successors(self) -> list:
    """
    Return all possible legal moves from the current state.
    Each move is represented as (action, next_state).
    action = (car_id, direction) e.g., ('A', 'up')
    """

    grid = self.get_grid()
    results = []

    for car_id, car in self.cars.items():

        # Horizontal cars
        if car.orientation == 'H':

            # Slide left
            if car.col > 0 and grid[car.row][car.col - 1] == '.':
                results.append(
                    ((car_id, 'left'), self._slide(car_id, 0, -1))
                )

            # Slide right
            right_end = car.col + car.length
            if right_end < BOARD_SIZE and grid[car.row][right_end] == '.':
                results.append(
                    ((car_id, 'right'), self._slide(car_id, 0, 1))
                )

        # Vertical cars
        else:

            # Slide up
            if car.row > 0 and grid[car.row - 1][car.col] == '.':
                results.append(
                    ((car_id, 'up'), self._slide(car_id, -1, 0))
                )

            # Slide down
            bottom_end = car.row + car.length
            if bottom_end < BOARD_SIZE and grid[bottom_end][car.col] == '.':
                results.append(
                    ((car_id, 'down'), self._slide(car_id, 1, 0))
                )

    return results
def _slide(self, car_id: str, dr: int, dc: int):
        """Return a new GameState with the specified car moved by (dr, dc)."""
        new_cars = [car.copy() for car in self.cars.values()]
        for car in new_cars:
            if car.car_id == car_id:
                car.row += dr
                car.col += dc
                break
        return GameState(new_cars)


