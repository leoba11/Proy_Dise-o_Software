from pieza import *

class PiezaGen():
    """
    Clase Pieza genérica:
        Crea ua pieza de cualquier tipo del MARDA con sus métodos.
    """
	
	# Constructor of the generic class
    def __init__(self, piezaConcreta):
        """
        Construye una pieza a partir de una pieza concreta.
        :param piezaConcreta: Pieza concreta con que se va a trabajar
        """
        
        self.piezaConcreta = piezaConcreta
        
    # Metod that invokes the concrete method of getting the color
    def getColor(self):
        """
        :return: Devuelve el color de la pieza
        """
        return self.piezaConcreta.getColor()
    
    # Method that invokes the concrete method of getting the x coord    
    def getCoordX(self):
        """
        :return: Devuelve la coordenada X de la pieza
        """
        return self.piezaConcreta.getCoordX()
    
    # Method that invokes the concrete method of getting the y coord
    def getCoordY(self):
        """
        :return: Devuelve la coordenada Y de la pieza
        """
        return self.piezaConcreta.getCoordY()
        
    # Method that invokes the concrete method of setting the x coord
    def setCoordX(self, nuevaCoordX):
        """
        Asigna una coordenada X a la pieza.
        :param nuevaCoordX: Nueva coordenada en X
        """
        return self.piezaConcreta.setCoordX(nuevaCoordX)
        
    # Method that invokes the concrete method of setting the y coord
    def setCoordY(self, nuevaCoordY):
        """
        Asigna una coordenada Y a la pieza.
        :param nuevaCoordY: Nueva coordenada en Y
        """
        return self.piezaConcreta.setCoordY(nuevaCoordY)
        
    # Method that invokes the concrete method of getting the piece's name
    def getName(self):
        """
        :return: Devuelve el nombre de la pieza
        """
        return self.piezaConcreta.getName()
	
	# Method that invokes the concrete method of getting the piece's type
    def getTipo(self):
        """
        :return: Devuelve el tipo de la pieza
        """
        return self.piezaConcreta.getTipo()

	# Method that invokes the concrete method of seeing if the piece is able to move
    def canMove(self, chessBoard):
        """
        Pregunta si la pieza puede moverse de manera válida, verifica si es su turno,
        si no hay obstáculos o enemigos.
        :param chessBoard: Tablero donde se va a mover la pieza
        :return: Boolean
        """
        return self.piezaConcreta.canMove(chessBoard)
	
	# Method that invokes the concrete method of moving the piece, by modifying its values
    def movePiece(self, newCoordinates):
        """
        Mueve la pieza.
        :param newCoordinates: Coordenadas a donde la va a mover.
        """
        return self.piezaConcreta.movePiece(newCoordinates)
    
    # Method that invokes the concrete method of getting the image    
    def getImage(self):
        """
        Devuelve la imagen de la pieza para poder así ser quitada del tablero.
        :return: La imagen
        """
        return self.piezaConcreta.getImage()
		
	# Function that checks if the pawn is allowed to do the double-step
    def noFirstMove(self):
        """
        Chequea si el peón puede hacer la primera jugada de moverse 2 cuadros.
        :return: Booleano
        """
        return self.piezaConcreta.noFirstMove()
