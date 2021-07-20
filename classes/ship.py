'''this file contains declaration of classes'''

class Ship:
    '''this is the class that difine a ship'''
    type="War ships"
    def __init__(self, serial_number , x_coordinate, y_coordinate, orientation):
        self.serial_number = serial_number
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.orientation = orientation
        self.still_floating = True
        self.out_of_the_map = False

    def process_order(self, order):
        """this function receives the order and applies it to the ship"""
        cardinal_points =["N", "E", "S", "W"]
        orientation_index = cardinal_points.index(self.orientation)
        if order == "TURN_LEFT":
            if orientation_index == 0:
                orientation_index = 4
            orientation_index = orientation_index - 1
            self.orientation = cardinal_points[orientation_index]
        if order == "TURN_RIGHT":
            if orientation_index == 3:
                orientation_index = -1
            orientation_index = orientation_index + 1
            self.orientation = cardinal_points[orientation_index]
        if order == "SUNK":
            self.still_floating = False
        if order == "MOVE_FORWARD":
            if self.orientation == "N":
                self.y_coordinate = self.y_coordinate + 1
            if self.orientation == "S":
                self.y_coordinate = self.y_coordinate - 1
            if self.orientation == "E":
                self.x_coordinate = self.x_coordinate + 1
            if self.orientation == "W":
                self.x_coordinate = self.x_coordinate - 1
