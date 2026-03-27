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
