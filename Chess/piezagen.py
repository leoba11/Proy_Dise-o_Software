from pieza import *

class PiezaGen():
	
	# Constructor of the generic class
    def __init__(self, piezaConcreta):
        
        self.piezaConcreta = piezaConcreta
        
    # Metod that invokes the concrete method of getting the color
    def getColor(self):
        return self.piezaConcreta.getColor()
    
    # Method that invokes the concrete method of getting the x coord    
    def getCoordX(self):
        return self.piezaConcreta.getCoordX()
    
    # Method that invokes the concrete method of getting the y coord
    def getCoordY(self):
        return self.piezaConcreta.getCoordY()
        
    # Method that invokes the concrete method of setting the x coord
    def setCoordX(self, nuevaCoordX):
        return self.piezaConcreta.setCoordX(nuevaCoordX)
        
    # Method that invokes the concrete method of setting the y coord
    def setCoordY(self, nuevaCoordY):
        return self.piezaConcreta.setCoordY(nuevaCoordY)
        
    # Method that invokes the concrete method of getting the piece's name
    def getName(self):
        return self.piezaConcreta.getName()
	
	# Method that invokes the concrete method of getting the piece's type
    def getTipo(self):
        return self.piezaConcreta.getTipo()

	# Method that invokes the concrete method of seeing if the piece is able to move
    def canMove(self, chessBoard):
        return self.piezaConcreta.canMove(chessBoard)
	
	# Method that invokes the concrete method of moving the piece, by modifying its values
    def movePiece(self, newCoordinates):
        return self.piezaConcreta.movePiece(newCoordinates)
    
    # Method that invokes the concrete method of getting the image    
    def getImage(self):
        return self.piezaConcreta.getImage()
		
	# Function that checks if the pawn is allowed to do the double-step
    def noFirstMove(self):
        return self.piezaConcreta.noFirstMove()
