import pygame
from Tile import Tile
from Board import Board
from math import *
from Geometry import *
from time import sleep
from random import *


colors = {'white': (255, 255, 255), 'black': (0, 0, 0), 'blue': (0, 0, 255), 'green': (0, 255, 0), 'yellow': (255, 0, 0)}


class BoardGraphical:
    def __init__(self, board: Board, sideLength: float):
        self.__board = board
        self.__sideLength = sideLength
        self.__upperLeftCenter = 0
        self.__display = None
        self.__hexWidth = 0
        self.__hexHeight = 0
        self.__boardHeight = 0
        self.__boardWidth = 0
        self._initializeCanvas()

    def _initializeTileDimensions(self):
        self.__hexWidth = triangleSideLength(self.__sideLength, self.__sideLength, 4 / 3 * pi)
        self.__hexHeight = 2 * self.__sideLength

    def _initializeBoardDimensions(self):
        self.__boardWidth = self.__hexWidth * (self.__board.MaximumWidth + 0.5)
        self.__boardHeight = 1.5 * self.__hexHeight * (self.__board.MaximumHeight // 2)
        if self.__board.MaximumHeight % 2 == 0:
            self.__boardHeight += 1 / 4 * self.__hexHeight
        else:
            self.__boardHeight += self.__hexHeight

    def _initializeCanvas(self):
        pygame.init()
        self._initializeTileDimensions()
        self._initializeBoardDimensions()
        self.__display = pygame.display.set_mode([int(self.__boardWidth), int(round(self.__boardHeight))])
        # self.__display.fill(colors['white'])
        self.__display.fill((255, 255, 255))

    def tileCenterCoordinates(self, line, index):
        '''
        computes the center of the tile at a given index on a given line
        :param line: int
        :param index: int
        :return: tuple of the coordinates of the hexagon center
        '''
        xCenter = index * self.__hexWidth + self.__hexWidth / 2
        yCenter = 1.5 * self.__hexHeight * (line // 2) + self.__hexHeight / 2
        if line % 2 == 1:
            xCenter += self.__hexWidth / 2
            yCenter += 3 / 4 * self.__hexHeight
        return xCenter, yCenter

    def tilePointsCoordinatesByCenter(self, center):
        '''
        returns a list of all 6 vertices of a hexagon with a given center
        :param center: tuple (x, y) of center coordinates
        :return: list of all 6 vertices of a hexagon with a given center
        '''
        pass
        xCenter = center[0]
        yCenter = center[1]
        x1 = xCenter
        y1 = yCenter - self.__hexHeight / 2
        x2 = xCenter + self.__hexWidth / 2
        y2 = yCenter - self.__sideLength / 2
        x3 = x2
        y3 = yCenter + self.__sideLength / 2
        x4 = xCenter
        y4 = yCenter + self.__hexHeight / 2
        x5 = xCenter - self.__hexWidth / 2
        y5 = y3
        x6 = x5
        y6 = y2
        return [(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5), (x6, y6)]

    def tilePointsCoordinates(self, line, index):
        '''
        returns a list of all 6 vertices of a hexagon at a given index on a given line
        :param line: int
        :param index: int
        :return: a list of all 6 vertices of a hexagon at a given index on a given line
        '''
        center = self.tileCenterCoordinates(line, index)
        return self.tilePointsCoordinatesByCenter(center)

    def drawTile(self, line, index, color):
        '''
        draws a tile on a given line at a given index in a given color
        :param line: int
        :param index: int
        :param color: RGB 3-tuple
        :return: None - tile is drawn on the display
        '''
        verticesCoordinates = self.tilePointsCoordinates(line, index)
        pygame.draw.polygon(self.__display, color, verticesCoordinates)

    def drawBoard(self):
        '''
        draws entire board - each tile has a random color
        :return: None - board is drawn on the display
        '''
        for line in range(self.__board.MaximumHeight):
            for index in range(self.__board.MaximumWidth):
                color = (randrange(0, 255), randrange(0, 255), randrange(0, 255))
                self.drawTile(line, index, color)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.__display.fill(colors['white'])
            # pygame.draw.circle(self.__display, (0, 0, 255), (30, 30), 20)
            '''
            self.drawTile(0, 0, colors['black'])
            self.drawTile(0, 1, colors['blue'])
            self.drawTile(0, 2, colors['green'])
            self.drawTile(1, 0, colors['yellow'])
            self.drawTile(2, 1, colors['green'])
            '''
            # sleep(3)
            self.drawBoard()
            pygame.display.flip()

        pygame.quit()
