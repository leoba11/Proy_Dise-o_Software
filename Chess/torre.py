from tkinter import *
from pieza import Pieza

import PIL.Image
import PIL.ImageTk

class Torre(Pieza):
	
	def __init__(self, name, color, coordX, coordY, imagen_archivo):
		self.name = name
		self.color = color
		self.coordX = coordX
		self.coordY = coordY
		#self.image = PhotoImage(file=imagen_archivo)
		image = PIL.Image.open(imagen_archivo)
		self.image = PIL.ImageTk.PhotoImage(image)
		self.image.photo = self.image
		self.noMove = True
        
        
	def printCoords(self):
		print("Color es: "+ self.getColor() + " y coordenadas(x,y) son: " + str(self.getCoordX()) + " " + str(self.getCoordY()))

	def getImage(self):
		return self.image
		
	# Function that returns if the Rook is allowed to do the castling-step
	def noFirstMove(self):
		if (self.getColor() == 'b' and (self.getCoordY() == 0 or self.getCoordY() == 7) and self.getCoordX() == 0 and self.noMove == True):
			return True
		if (self.getColor() == 'w' and (self.getCoordY() == 0 or self.getCoordY() == 7) and self.getCoordX() == 7 and self.noMove == True):
			return True
		return False
		
		
	# Function that returns the tuples with the possible moves of the piece
	def canMove(self, chessBoard):
		
		actual_coordX = self.getCoordX()
		actual_coordY = self.getCoordY()
		
		# Creates an empty list
		possible_moves = []
		
		# Sets the possible directions for movement
		coordsX = [0,-1,0,1]
		coordsY = [-1,0,1,0]
		
		# Checks each of the possible directions of movement
		for i in range(4):
			
			# Checks if the rook can move across the board
			for index in range(7):
				if ( chessBoard.isEmpty(actual_coordX + (coordsX[i] * (index + 1)), actual_coordY + (coordsY[i] * (index+1))) ):
					possible_moves.append( (actual_coordX + (coordsX[i] * (index + 1)), actual_coordY + (coordsY[i] * (index+1))) ) 
					
				else:
					if ( chessBoard.isEnemy(self.getColor(), actual_coordX + (coordsX[i] * (index + 1)), actual_coordY + (coordsY[i] * (index+1))) ):
						possible_moves.append( (actual_coordX + (coordsX[i] * (index + 1)), actual_coordY + (coordsY[i] * (index+1))) )
						break;
						
					else:
						break
					
		return possible_moves
		
		
	# Makes the rook movement
	def movePiece(self, newCoordinates):
		# Checks and sets the no movement variable
		if (self.noFirstMove()):
			self.noMove = False
		self.setCoordX(newCoordinates[0])
		self.setCoordY(newCoordinates[1])
		
'''root = Tk()
torrecita = Torre('b', 0, 7, "images/br.gif")
torrecita.printCoords()'''
		
