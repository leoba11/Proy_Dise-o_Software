from alfil import *
from caballo import *
from peon import *
from reina import *
from rey import *
from torre import *
from chessBoard import *
from tkinter import *
from tkinter import messagebox
from piezagen import PiezaGen

class tableroAbs(metaclass=ABCMeta):

    def __init__(self, rows = 8, cols = 8):
        self.board = []
        self.rows = rows
        self.cols = cols

        self.drawBoard()
        self.loadPieces()
        self.putPiecesOnBoard()

    @abstractmethod
    def drawBoard(self):
        pass

    @abstractmethod
    def loadPieces(self):
        pass

    @abstractmethod
    def putPiecesOnBoard(self):
        pass

    @abstractmethod
    def refreshBoard(self):
        pass

    @abstractmethod
    def drawBoard(self):
        pass

    @abstractmethod
    def add_piece(self, pieza, coordX, coordeY):
        pass

    @abstractmethod
    def isEmpty(self, coordX, coordY):
        pass

    @abstractmethod
    def isEnemy(self, color, coordX, coordY):
        pass

    @abstractmethod
    def savePosition(self, pieza):
        pass

    @abstractmethod
    def gameTest(self):
        pass

    @abstractmethod
    def logicEat(self, ate):
        pass
