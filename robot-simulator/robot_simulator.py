import math
# Globals for the bearings
# Change the values as you see fit
EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3


class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.coordinates = (x, y)

    def turn_right(self):
        self.bearing = ( self.bearing + 3 ) % 4

    def turn_left(self):
        self.bearing = ( self.bearing + 1) % 4

    def advance(self):
        self.coordinates = (round(self.coordinates[0] + math.cos(self.bearing * math.pi / 2)), round(self.coordinates[1] + math.sin(self.bearing * math.pi / 2)))

    def simulate(self, instructions):
        for instruction in instructions:
            if instruction == "R":
                self.turn_right()
            elif instruction == "L":
                self.turn_left()
            elif instruction == "A":
                self.advance()
            else:
                raise Exception("Wrong robot simulate intruction: " + instruction)
