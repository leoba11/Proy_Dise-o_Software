from abc import ABCMeta, abstractmethod


# Clase abstracta de vista del tablero, de la cual debe heredar chessBoard
class AbsChessBoard(metaclass=ABCMeta):

    
    self.color = ''
    self.oddColor = ''

    
    def getEvenColor(self):

        return self.color

    
    def getOddColor(self):

        return self.oddColor


    
    
    @abstractmethod
	def change_counter_loses(self, piece_dead_name):
		pass



	@abstractmethod
	def drawRectangle(self, x1, y1, x2, y2, color):
		pass



	@abstractmethod
	def addPiece(self, name, image, row, column):
		pass



	@abstractmethod
	def placePiece(self, name, row, column):
		pass



	@abstractmethod
	def loadInitPosPiece(self):
		pass



	@abstractmethod
	def refresh(self):
		pass


     @abstractmethod
    def printPieces(self):
		pass
