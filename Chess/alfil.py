from tkinter import *
from pieza import Pieza

class Alfil(Pieza):
	
	def __init__(self, color, coordX, coordY, imagen_archivo):
		self.color = color
		self.coordX = coordX
		self.coordY = coordY
		self.image = PhotoImage(file=imagen_archivo)
        
	def printCoords(self):
		print("Color es: "+ self.getColor() + " y coordenadas(x,y) son: " + str(self.getCoordX()) + " " + str(self.getCoordY()))
		
	# Function that returns the tuples with the possible moves of the piece
	def canMove(self, chessBoard):
		
		actual_coordX = self.getCoordX()
		actual_coordY = self.getCoordY()

		# Creates an empty list
		possible_moves = []
		
		# Sets the possible directions for movement
		coordsX = [-1,-1,1,1]
		coordsY = [-1,1,-1,1]
		
		# Checks each of the possible directions of movement
		for i in range(4):
			
			# Checks if the bishop can move across the board
			for index in range(7):
				if ( chessBoard.isEmpty(actual_coordX + (coordsX[i] * (index + 1)), actual_coordY + (coordsY[i] * (index+1))) ):
					possible_moves.append( (actual_coordX + (coordsX[i] * (index + 1)), actual_coordY + (coordsY[i] * (index+1))) )
					
				else:
					if ( chessBoard.isEnemy(self.getColor(), actual_coordX + (coordsX[i] * (index + 1)), actual_coordY + (coordsY[i] * (index+1))) ):
						possible_moves.append( (actual_coordX + (coordsX[i] * (index + 1)), actual_coordY + (coordsY[i] * (index+1))) )
						
					else:
						break
					
		return possible_moves
		
	# Makes the bishop movement
	def movePiece(self, newCoordinates):
		
		self.setCoordX(newCoordinates[0])
		self.setCoordY(newCoordinates[1])

root = Tk()
alfilito = Alfil('b', 0, 5, "images/bb.gif")
alfilito.printCoords()
