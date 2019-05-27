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
		
	def canMove(self):
		pass
		
	def getImage(self):
		return self.image
