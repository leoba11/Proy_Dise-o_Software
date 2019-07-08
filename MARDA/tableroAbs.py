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
from abc import ABCMeta, abstractmethod

class tableroAbs(metaclass=ABCMeta):
    """
    Clase Tablero Abstracto:
        Clase de la que van a heredar los demás tableros del MARDA, funciona como 
        "puente" o conexión principal de todos los juegos.
    """

    def __init__(self, rows, cols):
        """
        Constructor:
            Construye la clase y genera todos sus atributos.
            El tablero como tal es una matriz :board:
            Se llam a los métodos:
                + drawBoard
                + loadPieces
                + putPiecesOnBoard
            :param rows: Filas para el tamaño.
            :param cols: Columnas para el tamaño.
        """
        self.board = [] # tabla general
        self.rows = rows # cantidad de filas
        self.cols = cols # cantidad de columnas

        self.drawBoard()
        self.loadPieces()
        self.putPiecesOnBoard()

    # Método para controlar donde van a quedar espacios vacios una vez que se coloquen las piezas
    @abstractmethod
    def drawBoard(self):
        """
        Dibuja el tablero, cada juego del MARDA lo hará a su conveniencia.
        Controla los escpacios vacíos que va a tener el tablero.
        """
        pass

    # Método para inicializar toda la información necesaria de cada pieza o grupo de piezas
    @abstractmethod
    def loadPieces(self):
        """
        Inicializa toda la información que requiere cada pieza de cada juego del MARDA.
        """
        pass

    # Método para colocar todas las piezas en el tablero
    @abstractmethod
    def putPiecesOnBoard(self):
        """
        Pone las piezas en el table, como sea necesario para cada juego.
        """
        pass

    # Método para refrescar el tablero
    @abstractmethod
    def refreshBoard(self):
        """
        Refresca el tablero después de cada evento, ya sea moverse, comer o revisar posibles movimientos.
        """
        pass

    # Método para colocar una pieza específica en el tablero dada sus coordenadas
    @abstractmethod
    def add_piece(self, pieza, coordX, coordeY):
        """
        Coloca una pieza específica en el tablero, con sus coordenadas específicas.
        """
        pass

    # Método para verificar si un espacio del tablero está vacío dada sus coordenadas
    @abstractmethod
    def isEmpty(self, coordX, coordY):
        """
        Pregunta si un espacio del tablero está vacío o no.
        :return: Booleano
        """
        pass

    # Método para verificar si en una posición del tablero hay una pieza del jugador contrario
    @abstractmethod
    def isEnemy(self, color, coordX, coordY):
        """
        Verifica si en la posición dada hay un enemigo o no.
        :param color: Color de la pieza para determinar si es o no enemigo.
        :param coordX/Y: Coordenadas para hacer la verificación
        :return: Booleano
        """
        pass

    # Método para guardar la posición de una pieza específica
    @abstractmethod
    def savePosition(self, pieza):
        """
        Salva la posición de una pieza.
        :param pieza: La piza que se va a salvar
        """
        pass

    # Método para crear pruebas del juego
    @abstractmethod
    def gameTest(self):
        """
        Genera una prueba rápida en el tablero.
        """
        pass

    # Método para "comer" o ganarle una pieza al jugador oponente
    @abstractmethod
    def logicEat(self, ate):
        """
        Hace un comido lógico en el tablero.
        """
        pass
