from pygame import *


class Tile:
    def __init__(self, value=None):
        self.neighbours = {'NW': None,
                           'W': None,
                           'SW': None,
                           'SE': None,
                           'E': None,
                           'NE': None}
        self.NW = None
        self.W = None
        self.SW = None
        self.SE = None
        self.E = None
        self.NE = None
        self.value = value

