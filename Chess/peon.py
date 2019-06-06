from tkinter import *
from pieza import Pieza

import PIL.Image
import PIL.ImageTk

class Peon(Pieza):
	
	def __init__(self, color, coordX, coordY, imagen_archivo):
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
		
	# Function that checks if the pawn is allowed to do the double-step
	def noFirstMove(self):
		if (self.getColor() == 'b' and self.getCoordX() == 1 and self.noMove == True):
			return True
		if (self.getColor() == 'w' and self.getCoordX() == 6 and self.noMove == True):
			return True
		return False
		
		
    # Checks if pawn can move, and returns the coordinates of possible moves for the pawn
	def canMove(self, chessBoard):
		actual_coordX = self.getCoordX()
		actual_coordY = self.getCoordY()
		
		# Creates an empty list
		possible_moves = []
		
		# Sets the direction of the pawn, checking if it is a black one or a white one
		direction = 1 if (self.getColor() == 'b') else -1
		
		# Checks if the board at the position requested is empty or not
		if ( self.noFirstMove() and chessBoard.isEmpty(actual_coordX + 2 * (direction), actual_coordY) ) :
			possible_moves.append((actual_coordX + direction, actual_coordY ))
			possible_moves.append((actual_coordX + (direction * 2), actual_coordY ))
			
		else:
			if ( chessBoard.isEmpty(actual_coordX + direction, actual_coordY) ) :
				possible_moves.append((actual_coordX + direction, actual_coordY ))
		
		# Checks if it can moves to a position for eating another piece (left)			
		if ( chessBoard.isEnemy(self.getColor(), actual_coordX + direction, actual_coordY - 1) ):
			possible_moves.append((actual_coordX + direction, actual_coordY - 1))
			
		# Checks if it can moves to a position for eating another piece (right)			
		if ( chessBoard.isEnemy(self.getColor(), actual_coordX + direction, actual_coordY + 1) ):
			possible_moves.append((actual_coordX + direction, actual_coordY + 1))
			
		# It has to be checked if the pawn makes it to the final, in order to convert it into a Queen
		print(possible_moves)
		
		return possible_moves
		
	# Makes the pawn movement
	def movePiece(self, newCoordinates):
		# Checks and sets the no movement variable
		if (self.noFirstMove()):
			self.noMove = False
		self.setCoordX(newCoordinates[0])
		self.setCoordY(newCoordinates[1])

'''
root = Tk()
peoncito = Peon('b', 1, 4, "images/bp.gif")
peoncito.printCoords()'''
