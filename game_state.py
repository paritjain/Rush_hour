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
