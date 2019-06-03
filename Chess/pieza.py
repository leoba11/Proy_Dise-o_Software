from abc import ABCMeta, abstractmethod

# Clase pieza de la cual heredaran las demás piezas del ajedrez
# Tiene un color, una coordenadaX, una coordenadaY
class Pieza(metaclass=ABCMeta):
	
	color = ''
	coordX = 0
	coordY = 0
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

	@abstractmethod
	def canMove(self):
		pass
	
	@abstractmethod
	def movePiece(self, newCoordinates):
		pass
		
		
##piece = Pieza('b', 1, 6)

##print("Color es: "+ piece.getColor() + " y coordenadas(x,y) son: " + str(piece.getCoordX()) + " " + str(piece.getCoordY()))
