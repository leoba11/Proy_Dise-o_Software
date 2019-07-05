from logicChessBoard import *

class genBoard():

    #Constructor
    def __init__(self, tableroConcreto):
        
        self.tableroConcreto = tableroConcreto

    # Method that invokes the "Refresh board" method of the concrete board
    def refreshBoard(self):
        
        return self.tableroConcreto.refreshBoard()
        
        
    # Method that invokes the "changeTowerPosition" method of the concrete board
    def changeTowerPosition(self,direction, orientation, coord_y_tower, coord_x, coord_y):
        
        return self.tableroConcreto.changeTowerPosition(direction, orientation, coord_y_tower, coord_x, coord_y)
        
        
    # Method that invokes the "drawBoard" method of the concrete board
    def drawBoard(self):
		
        return self.tableroConcreto.drawBoard(self)
