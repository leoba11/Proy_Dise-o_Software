from logicChessBoard import *

class GenericBoard():

    #Constructor
    def __init__(self, tableroConcreto, rows, cols):
        
        self.tableroConcreto = tableroConcreto
        self.board = self.tableroConcreto.board
        self.rows = rows
        self.cols = cols

    # Method that invokes or uses the "Refresh board" method of the concrete board
    def refreshBoard(self):
        
        return self.tableroConcreto.refreshBoard()
        
        
    # Method that invokes or uses the "changeTowerPosition" method of the concrete board
    def changeTowerPosition(self,direction, orientation, coord_y_tower, coord_x, coord_y):
        
        return self.tableroConcreto.changeTowerPosition(direction, orientation, coord_y_tower, coord_x, coord_y)
        
        
    # Method that invokes or uses the "drawBoard" method of the concrete board
    def drawBoard(self):
		
        return self.tableroConcreto.drawBoard(self)
        
    
    # Method that invokes or uses the "add piece" method of the concrete board
    def add_piece(self, pieza, coordX, coordY):
        
        return self.tableroConcreto.add_piece(pieza, coordX, coordY)
    
    
    # Method that invokes or uses the "is Empty" method of the concrete board
    def isEmpty(self, coordX, coordY):
        
        return self.tableroConcreto.isEmpty(coordX, coordY)
        
    
    # Method that invokes or uses the "is Enemy" method of the concrete board
    def isEnemy(self, color, coordX, coordY):
        
        return self.tableroConcreto.isEnemy(color, coordX, coordY)
        
    
    # Method that invokes or uses the "save position" method of the concrete board
    def savePosition(self, pieza):
        
        return self.tableroConcreto.savePosition(pieza)
    
    
    # Method that invokes or uses the "load Pieces" method of the concrete board
    def loadPieces(self):
        
        return self.tableroConcreto.loadPieces()
        
    
    # Method that invokes or uses the "put pieces on board" method of the concrete board
    def putPiecesOnBoard(self):
        
        return self.tableroConcreto.putPiecesOnBoard()
        
    # Method that invokes or uses the "game test" method of the concrete board
    def gameTest(self):
        
        return self.tableroConcreto.gameTest()
        
    # Method that invokes or uses the "chess piece king" method of the concrete board
    def checkPieceKing(self, coord_x, coord_y):
        
        return self.tableroConcreto.checkPieceKing(coord_x, coord_y)
        
    # Method that invokes or uses the "returnPositionsKingThreatened" method of the concrete board
    def returnPositionsKingThreatened(self):
        
        return self.tableroConcreto.returnPositionsKingThreatened()
    
    # Method that invokes or uses the "set position king" method of the concrete board    
    def setPositionKing(self, color, coord_x, coord_y):
        
        return self.tableroConcreto.setPositionKing(color, coord_x, coord_y)
        
        
    # Method that invokes or uses the "get potential king threatened" method of the concrete board
    def getPotentialKingThreatened(self):
        
        return self.tableroConcreto.getPotentialKingThreatened()
