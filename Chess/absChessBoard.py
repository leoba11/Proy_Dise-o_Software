from abc import ABCMeta, abstractmethod


# Clase abstracta de vista del tablero, de la cual debe heredar chessBoard
class AbsChessBoard(metaclass=ABCMeta):
    """
    Clase Abstracta de Tablero de Ajedrez:
        Clase de vista del tablero, hereda de la clase ChessBoard.
        Se encarga de la parte gráfica del tablero de Ajedrez del MARDA.
        Cuenta con 2 atributos:
            + color: El color negro, o algún otro que se escoja.
            + oddColor: Color blanco, o algún otro que se escoja.
    """

    
    color = ''
    oddColor = ''

    
    def getEvenColor(self):
        """
        Obtiene el color par.
        :return: Color
        """

        return self.color

    
    def getOddColor(self):
        """
        Obtiene el color impar.
        :return: Color
        """
        return self.oddColor

    
    @abstractmethod
    def change_counter_loses(self, piece_dead_name):
        """
        Cambia el contador de las piezas comidas.
        :param piece_dead_name: Pieza que se comió.
        """
        pass

    @abstractmethod
    def drawRectangle(self, x1, y1, x2, y2, color):
        """
        Dibuja un rectángulo que sera usado en el canvas.
        :param x1, y1, x2, y2: Dimensiones de los rectángulos de colores.
        :param color: Color del rectágulo que se va a dibujar, 
        """

        pass

    @abstractmethod
    def addPiece(self, name, image, row, column):
        """
        Agrega una pieza al vector de piezas.
        :param name: Nombre de la pieza.
        :param image: Le asiga una imagen a la pieza
        :param row/column: Coordenadas de la pieza.
        """
        pass

    @abstractmethod
    def placePiece(self, name, row, column):
        """
        Pone y dibuja la pieza con su imagen en el tablero.
        :param name: Nombre de la pieza a poner
        :param row/colum: Coordenadas de la pieza a poner
        """
        pass

    @abstractmethod
    def loadInitPosPiece(self):
        """
        Carga las posiciones iniciales de cada pieza
        """
        pass

    @abstractmethod
    def refresh(self):
        """
        Refreca los dibujos del tablero.
        """
        pass

    @abstractmethod    
    def printPieces(self):
        """
        Imprime todas las piezas que hay en el vector.
        """
        pass
