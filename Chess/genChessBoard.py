from chessBoard impor *


class GenChessBoard():
    
    #Constructor
    def __init__(self, chessBoardConcreto):

        self.chessBoardConcreto = chessBoardConcreto

    def change_counter_loses(self, piece_dead_name):

        return self.chessBoardConcreto.change_counter_loses(piece_dead_name)

    
    def drawRectangle(self, x1, y1, x2, y2, color):
        
        return self.chessBoardConcreto.drawRectangle(x1, y1, x2, y2, color)

    
    def addPiece(self, name, image, row, column):

        return self.chessBoardConcreto.addPiece(name, image, row, column)

    
    def placePiece(self, name, row, column):

        return self.chessBoardConcreto.placePiece(name, row, column)

    def loadInitPosPiece(self):
        
        return chessBoardConcreto.loadInitPosPiece()

    def printPieces(self):

        return chessBoardConcreto.printPieces()

    def refresh(self):
        
        return chessBoardConcreto.refresh()

    def getEvenColor(self):

        return chessBoardConcreto.getEvenColor()

    
    def getOddColor(self):
        return chessBoardConcreto.getOddColor()
