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

    def __init__(self, rows, cols):
        self.board = [] # tabla general
        self.rows = rows # cantidad de filas
        self.cols = cols # cantidad de columnas

        # secuencia general de llamado a los métodos
        self.drawBoard()
        self.loadPieces()
        self.putPiecesOnBoard()

    # Método para controlar donde van a quedar espacios vacios una vez que se coloquen las piezas
    @abstractmethod
    def drawBoard(self):
        pass

    # Método para inicializar toda la información necesaria de cada pieza o grupo de piezas
    @abstractmethod
    def loadPieces(self):
        pass

    # Método para colocar todas las piezas en el tablero
    @abstractmethod
    def putPiecesOnBoard(self):
        pass

    # Método para refrescar el tablero
    @abstractmethod
    def refreshBoard(self):
        pass

    # Método para colocar una pieza específica en el tablero dada sus coordenadas
    @abstractmethod
    def add_piece(self, pieza, coordX, coordeY):
        pass

    # Método para verificar si un espacio del tablero está vacío dada sus coordenadas
    @abstractmethod
    def isEmpty(self, coordX, coordY):
        pass

    # Método para verificar si en una posición del tablero hay una pieza del jugador contrario
    @abstractmethod
    def isEnemy(self, color, coordX, coordY):
        pass

    # Método para guardar la posición de una pieza específica
    @abstractmethod
    def savePosition(self, pieza):
        pass

    # Método para crear pruebas del juego
    @abstractmethod
    def gameTest(self):
        pass

    # Método para "comer" o ganarle una pieza al jugador oponente
    @abstractmethod
    def logicEat(self, ate):
        pass
