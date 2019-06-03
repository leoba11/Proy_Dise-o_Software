from tkinter import *
from pieza import Pieza

class Reina(Pieza):
	
	def __init__(self, color, coordX, coordY, imagen_archivo):
		self.color = color
		self.coordX = coordX
		self.coordY = coordY
		self.image = PhotoImage(file=imagen_archivo)
	
	
	def printCoords(self):
		print("Color es: "+ self.getColor() + " y coordenadas(x,y) son: " + str(self.getCoordX()) + " " + str(self.getCoordY()))
	
		
	# Function that returns the tuples with the possible moves of the piece
	def canMove(self):
		
		actual_coordX = self.getCoordX()
		actual_coordY = self.getCoordY()
		
		# Creates an empty list
		possible_moves = []
		
		# Sets the possible coordenates of the movements for the queen
		coordsX = [-1, 0, 1, -1, 1, -1, 0, 1]
		coordsY = [-1, -1, -1, 0, 0, 1, 1, 1]
		
		# Checks each of the possible directions of movement
		for i in range(8):
			
			# Checks if the queen can move across the board
			for index in range(7):
				if ( chessBoard.isEmpty(actual_coordX + (coordsX[i] * (index + 1)), actual_coordY + (coordsY[i] * (index+1))) ):
					possible_moves.append( (actual_coordX + (coordsX[i] * (index + 1)), actual_coordY + (coordsY[i] * (index+1))) ) 
					
				else:
					if ( chessBoard.isEnemy(self.getColor(), actual_coordX + (coordsX[i] * (index + 1)), actual_coordY + (coordsY[i] * (index+1))) ):
						possible_moves.append( (actual_coordX + (coordsX[i] * (index + 1)), actual_coordY + (coordsY[i] * (index+1))) )
						
					else:
						break
					
		return possible_moves
		
	
	# Makes the queen movement
	def movePiece(self, newCoordinates):
		
		self.setCoordX(newCoordinates[0])
		self.setCoordY(newCoordinates[1])

'''root = Tk()
reinita = Reina('b', 0, 3, "images/bq.gif")
reinita.printCoords()'''
