from abc import ABCMeta, abstractmethod

# Clase pieza de la cual heredaran las demás piezas del ajedrez
# Tiene un color, una coordenadaX, una coordenadaY
class Pieza(metaclass=ABCMeta):
	
	color = ''
	coordX = 0
	coordY = 0
	name = ''
	isPlaying = True
		
	def getColor(self):
		return self.color
		
	def getCoordX(self):
		return self.coordX
	
	def getCoordY(self):
		return self.coordY
		
	def setCoordX(self, nuevaCoordX):
		self.coordX = nuevaCoordX
	
	def setCoordY(self, nuevaCoordY):
		self.coordY = nuevaCoordY
	
	def getName(self):
		return self.name

	@abstractmethod
	def canMove(self):
		pass
	
	@abstractmethod
	def movePiece(self, newCoordinates):
		pass

