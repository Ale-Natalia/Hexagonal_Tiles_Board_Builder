from Board import Board
from pygame import *
from Draw import BoardGraphical

width = int(input("Maximum width: "))
height = int(input("Maximum height: "))
board = Board(width, height)
drawer = BoardGraphical(board, 20)
drawer.run()
