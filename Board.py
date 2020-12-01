from Tile import Tile


class Board:
    def __init__(self, maximumWidth, maximumHeight):
        self.__maximumWidth = maximumWidth
        self.__maximumHeight = maximumHeight
        self.__lineHeads = [None] * self.__maximumHeight
        self.__mainDiagonalHeads = [None] * self.__maximumWidth
        self.__secondaryDiagonalHeads = [None] * self.__maximumWidth
        self.__lineTails = [None] * self.__maximumHeight
        self.__mainDiagonalTails = [None] * self.__maximumWidth
        self.__secondaryDiagonalTails = [None] * self.__maximumWidth
        pass
        self._buildBoard()

    @property
    def MaximumWidth(self):
        return self.__maximumWidth

    @MaximumWidth.setter
    def MaximumWidth(self, value):
        self.__maximumWidth = value

    @property
    def MaximumHeight(self):
        return self.__maximumHeight

    @MaximumHeight.setter
    def MaximumHeight(self, value):
        self.__maximumHeight = value

    def _buildFirstOddLine(self):
        '''
        we build the first line of the board + add diagonal heads
        :return: None - we update the attributes
        '''
        currentHead = Tile()
        self.__mainDiagonalHeads[0] = currentHead
        self.__secondaryDiagonalHeads[0] = currentHead
        self.__lineHeads[0] = currentHead
        previousHead = currentHead
        for diagonalIndex in range(1, self.__maximumWidth):
            currentHead = Tile()
            previousHead.neighbours['E'] = currentHead
            currentHead.neighbours['W'] = previousHead
            self.__mainDiagonalHeads[diagonalIndex] = currentHead
            self.__secondaryDiagonalHeads[diagonalIndex] = currentHead
            previousHead = currentHead

    def _buildEvenLine(self, lineIndex):
        '''
        we build an even line of the board
        :param lineIndex: integer
        :return: None - we update the attributes
        '''
        currentTile = Tile()
        self.__lineHeads[lineIndex] = currentTile
        tileAbove = self.__lineHeads[lineIndex - 1]
        tileAbove.neighbours['SE'] = currentTile
        currentTile.neighbours['NW'] = tileAbove
        previousTile = currentTile
        for tileIndex in range(1, self.__maximumWidth):
            currentTile = Tile()
            tileAbove = tileAbove.neighbours['E']
            previousTile.neighbours['NE'] = tileAbove
            previousTile.neighbours['E'] = currentTile
            currentTile.neighbours['W'] = previousTile
            currentTile.neighbours['NW'] = tileAbove
            tileAbove.neighbours['SW'] = previousTile
            tileAbove.neighbours['SE'] = currentTile
            previousTile = currentTile

    def _buildOddLine(self, lineIndex):
        '''
        we build an odd line of the board
        :param lineIndex: integer
        :return: None - we update
        '''
        currentTile = Tile()
        self.__lineHeads[lineIndex] = currentTile
        tileAbove = self.__lineHeads[lineIndex - 1]
        tileAbove.neighbours['SW'] = currentTile
        currentTile.neighbours['NE'] = tileAbove
        previousTile = currentTile
        for tileIndex in range(1, self.__maximumWidth):
            currentTile = Tile()
            currentTile.neighbours['W'] = previousTile
            previousTile.neighbours['E'] = currentTile
            currentTile.neighbours['NW'] = tileAbove
            tileAbove.neighbours['SE'] = currentTile
            tileAbove = tileAbove.neighbours['E']
            currentTile.neighbours['NE'] = tileAbove
            tileAbove.neighbours['SW'] = currentTile
            previousTile = currentTile

    def _buildBoard(self):
        '''
        we build a board of the given size of empty tiles
        the odd lines are on the first main diagonal
        the even lines are on the second main diagonal
        :return: None - we update directly the attributes
        '''
        self._buildFirstOddLine()
        setsOfTwoLines = (self.__maximumHeight - 1) // 2
        remainingLine = True if (self.__maximumHeight - 1) % 2 == 1 else False
        for setOfLines in range(setsOfTwoLines):
            self._buildEvenLine(setOfLines * 2 + 1)
            self._buildOddLine(setOfLines * 2 + 2)
        if remainingLine:
            self._buildEvenLine(self.__maximumHeight - 1)

    def checkValidCoordinates_Add(self, line, mainDiagonal, secondaryDiagonal):
        '''
        checks if a given set of coordinates is valid for adding a new tile
        :param line: integer
        :param mainDiagonal: integer
        :param secondaryDiagonal: integer
        :return: raises exception if invalid
        '''
        pass

    def neighboursOfTile(self, line, mainDiagonal, secondaryDiagonal):
        '''
        returns a dictionary of neighbours
        :param line: integer
        :param mainDiagonal: integer
        :param secondaryDiagonal: integer
        :return: boolean
        '''

    def getTile(self, line, mainDiagonal, secondaryDiagonal):
        '''
        gets the tile at a certain set of coordinates/
        creates an empty one with the corresponding neighbours if it doesn't exist but can be created
        :param line: integer
        :param mainDiagonal: integer
        :param secondaryDiagonal: integer
        :return: the tile object + True/False (it existed before or it got created)
                throws exception if tile doesn't exist and can't be added
        '''

    def addTile(self, line, mainDiagonal, secondaryDiagonal, value):
        self.checkValidCoordinates_Add(line, mainDiagonal, secondaryDiagonal)
