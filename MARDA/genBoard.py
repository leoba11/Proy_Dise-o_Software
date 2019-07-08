from logicChessBoard import *

class GenericBoard():
    """
    Clase Tablero Genérico:
        Esta es la clase que usan los demás juegos del MARDA para lograr crear y controlar 
        su tablero.
        Todos los métodos de esta clase invocan al método concreto del juego especificado.
        Sus atributos son:
            + tableroConcreto
            + rows
            + cols
    """

    #Constructor
    def __init__(self, tableroConcreto, rows, cols):
        """
        Inicializa todos los atributos antes mencionados.
        """
        self.tableroConcreto = tableroConcreto
        self.board = self.tableroConcreto.board
        self.rows = rows
        self.cols = cols

    # Method that invokes or uses the "Refresh board" method of the concrete board
    def refreshBoard(self):
        """
        Refresca el tablero y los vectores de piezas después de cada evento.
        """
        return self.tableroConcreto.refreshBoard()
        
        
    # Method that invokes or uses the "changeTowerPosition" method of the concrete board
    def changeTowerPosition(self,direction, orientation, coord_y_tower, coord_x, coord_y):
        """
        Para poder crear un buen "enroke"
        """
        return self.tableroConcreto.changeTowerPosition(direction, orientation, coord_y_tower, coord_x, coord_y)
        
        
    # Method that invokes or uses the "drawBoard" method of the concrete board
    def drawBoard(self):
        """
        Para dibujar el tablero gráfico.
        """
		
        return self.tableroConcreto.drawBoard(self)
        
    
    # Method that invokes or uses the "add piece" method of the concrete board
    def add_piece(self, pieza, coordX, coordY):
        """
        Agrega ina pieza al vector.
        :param pieza: La pieza que se va a agregar
        :param coordX/CoordY: Coordenadas donde la pieza se va a poner.
        """
        return self.tableroConcreto.add_piece(pieza, coordX, coordY)
    
    # Method that invokes or uses the "is Empty" method of the concrete board
    def isEmpty(self, coordX, coordY):
        """
        Pregunta si una posición del tablero está vacía.
        :param coordX/Y: Posición donde se pregunta.
        """
        
        return self.tableroConcreto.isEmpty(coordX, coordY)
        
    
    # Method that invokes or uses the "is Enemy" method of the concrete board
    def isEnemy(self, color, coordX, coordY):
        """
        Pregunta en la posición dada si hay un enemigo.
        :param color: Color para saber si es enemigo o no
        :param coordX/Y: Posición a preguntar
        """
        return self.tableroConcreto.isEnemy(color, coordX, coordY)
        
    
    # Method that invokes or uses the "save position" method of the concrete board
    def savePosition(self, pieza):
        """
        Salva la posición de la pieza acutal.
        :param pieza: Pieza de la que se va a salvar la posición
        """
        return self.tableroConcreto.savePosition(pieza)
    
    
    # Method that invokes or uses the "load Pieces" method of the concrete board
    def loadPieces(self):
        """
        Carga las piezas en el vector de piezas.
        """
        return self.tableroConcreto.loadPieces()
        
    
    # Method that invokes or uses the "put pieces on board" method of the concrete board
    def putPiecesOnBoard(self):
        """
        Pone las piezas en el tablero.
        """
        return self.tableroConcreto.putPiecesOnBoard()
        
    # Method that invokes or uses the "game test" method of the concrete board
    def gameTest(self):
        """
        Hace una pequeña prueba de algunas posiciones
        """
        return self.tableroConcreto.gameTest()
        
    # Method that invokes or uses the "chess piece king" method of the concrete board
    def checkPieceKing(self, coord_x, coord_y):
        """
        Revisa si la pieza seleccionada es el rey, para juadas como jaque o enroque.
        :param coordX/coordY: Donde está el rey.
        """
        return self.tableroConcreto.checkPieceKing(coord_x, coord_y)
        
    # Method that invokes or uses the "returnPositionsKingThreatened" method of the concrete board
    def returnPositionsKingThreatened(self):
        """
        Retorna las coordenadas del rey que esta en amenaza.
        :return coordenadas:
        """
        return self.tableroConcreto.returnPositionsKingThreatened()
    
    # Method that invokes or uses the "set position king" method of the concrete board    
    def setPositionKing(self, color, coord_x, coord_y):
        """
        Setea la posción del rey para un enroque
        :param color: Color del rey
        :param coord_x/_y: coordenada de x y x
        """        
        return self.tableroConcreto.setPositionKing(color, coord_x, coord_y)
        
        
    # Method that invokes or uses the "get potential king threatened" method of the concrete board
    def getPotentialKingThreatened(self):
        """
        Revisa si el rey está en una posbible amenaza.
        """
        return self.tableroConcreto.getPotentialKingThreatened()
