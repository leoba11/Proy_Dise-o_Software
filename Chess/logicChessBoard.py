from alfil import *
from caballo import *
from peon import *
from reina import *
from rey import *
from torre import *
from chessBoard import *
from tkinter import *

#Se inicializa en 0's para evitar problemas
#Variables globales
piecesforLogic = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
#board = []

class logicChessBoard():

    def __init__(self, rows = 8, cols = 8):
        self.board = []
        self.rows = rows
        self.cols = cols
        
        self.loadPieces()
        self.drawBoard()
        self.putPiecesOnBoard()
        self.gameTest()

    def drawBoard(self):
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append('*')
            self.board.append(row)
        #print(self.board)
        
    def add_piece(self, pieza, coordX, coordY):
        if(not (math.isnan(self.tablero[coordX][coordY]))):
            self.board[coordX][coordY] = pieza
    
    def isEmpty(self, coordX, coordY):
        #print (coordX, coordY)
        if (coordX < 0  or coordX > 7 or coordY < 0 or coordY > 7):
            return False
        else:
            if(self.board[coordX][coordY] == '*'):#type(14)):
                return True
            else:
                return False


    def isEnemy(self, color, coordX, coordY):
        if (coordX < 0  or coordX > 7 or coordY < 0 or coordY > 7):
            return False
        if(self.board[coordX][coordY] == '*'):
            return False
        else:
            if (self.board[coordX][coordY].getColor() != color):
                return True
            else:
                return False

    def loadPieces(self):
        root = Tk()
        global piecesforLogic

        #--------------------Black Empire-----------------------------
        self.black_king = Rey('b', 0, 4, "pieces/icons8-rey-48.png")
        piecesforLogic[0] = self.black_king

        self.black_queen = Reina('b', 0,3, "pieces/icons8-reina-48.png")
        piecesforLogic[1] = self.black_queen
        #piecesforLogic[1] = '*'

        self.black_bishop1 = Alfil('b', 0, 2, "pieces/icons8-obispo-48.png")
        piecesforLogic[2] = self.black_bishop1
        #piecesforLogic[2] = '*'

        self.black_bishop2 = Alfil('b', 0, 5, "pieces/icons8-obispo-48.png")
        piecesforLogic[3] = self.black_bishop2
        #piecesforLogic[3] = '*'

        self.black_knight1 = Caballo('b', 0, 1, "pieces/icons8-caballero-48.png")
        piecesforLogic[4] = self.black_knight1
        #piecesforLogic[4] = '*'

        self.black_knight2 = Caballo('b', 0, 6, "pieces/icons8-caballero-48.png")
        piecesforLogic[5] = self.black_knight2
        #piecesforLogic[5] = '*'

        self.black_rook1 = Torre('b', 0, 0, "pieces/icons8-torre-48.png")
        piecesforLogic[6] = self.black_rook1

        self.black_rook2 = Torre('b', 0, 7, "pieces/icons8-torre-48.png")
        piecesforLogic[7] = self.black_rook2

        self.black_pawn1 = Peon('b', 1, 0, "pieces/icons8-peón-48.png")
        piecesforLogic[8] = self.black_pawn1

        self.black_pawn2 = Peon('b', 1, 1, "pieces/icons8-peón-48.png")
        piecesforLogic[9] = self.black_pawn2

        self.black_pawn3 = Peon('b', 1, 2, "pieces/icons8-peón-48.png")
        piecesforLogic[10] = self.black_pawn3

        self.black_pawn4 = Peon('b', 1, 3, "pieces/icons8-peón-48.png")
        piecesforLogic[11] = self.black_pawn4
        #piecesforLogic[11] = '*'

        self.black_pawn5 = Peon('b', 1, 4, "pieces/icons8-peón-48.png")
        piecesforLogic[12] = self.black_pawn5
        #piecesforLogic[12] = '*'

        self.black_pawn6 = Peon('b', 1, 5, "pieces/icons8-peón-48.png")
        piecesforLogic[13] = self.black_pawn6
        #piecesforLogic[13] = '*'

        self.black_pawn7 = Peon('b', 1, 6, "pieces/icons8-peón-48.png")
        piecesforLogic[14] = self.black_pawn7

        self.black_pawn8 = Peon('b', 1, 7, "pieces/icons8-peón-48.png")
        piecesforLogic[15] = self.black_pawn8
        #piecesforLogic[15] = '*'
        #--------------------Black Empire-----------------------------
        #--------------------White Empire-----------------------------
        self.white_king = Rey('w', 7, 4, "pieces/icons8-rey-48 (1).png")
        piecesforLogic[16] = self.white_king

        self.white_queen = Reina('w', 7,3, "pieces/icons8-reina-48 (1).png")
        piecesforLogic[17] = self.white_queen

        self.white_bishop1 = Alfil('w', 7, 2, "pieces/icons8-obispo-48 (1).png")
        piecesforLogic[18] = self.white_bishop1

        self.white_bishop2 = Alfil('w', 7, 5, "pieces/icons8-obispo-48 (1).png") 
        piecesforLogic[19] = self.white_bishop2

        self.white_knight1 = Caballo('w', 7, 1, "pieces/icons8-caballero-48 (1).png")
        piecesforLogic[20] = self.white_knight1

        self.white_knight2 = Caballo('w', 7, 6, "pieces/icons8-caballero-48 (1).png")
        piecesforLogic[21] = self.white_knight2

        self.white_rook1 = Torre('w', 7, 0, "pieces/icons8-torre-48 (1).png")
        piecesforLogic[22] = self.white_rook1

        self.white_rook2 = Torre('w', 7, 7, "pieces/icons8-torre-48 (1).png")
        piecesforLogic[23] = self.white_rook2

        self.white_pawn1 = Peon('w', 6, 0, "pieces/icons8-peón-48 (1).png")
        piecesforLogic[24] = self.white_pawn1

        self.white_pawn2 = Peon('w', 6, 1, "pieces/icons8-peón-48 (1).png")
        piecesforLogic[25] = self.white_pawn2

        self.white_pawn3 = Peon('w', 6, 2, "pieces/icons8-peón-48 (1).png")
        piecesforLogic[26] = self.white_pawn3

        self.white_pawn4 = Peon('w', 6, 3, "pieces/icons8-peón-48 (1).png")
        piecesforLogic[27] = self.white_pawn4

        self.white_pawn5 = Peon('w', 6, 4, "pieces/icons8-peón-48 (1).png")
        piecesforLogic[28] = self.white_pawn5

        self.white_pawn6 = Peon('w', 6, 5, "pieces/icons8-peón-48 (1).png")
        piecesforLogic[29] = self.white_pawn6

        self.white_pawn7 = Peon('w', 6, 6, "pieces/icons8-peón-48 (1).png")
        piecesforLogic[30] = self.white_pawn7

        self.white_pawn8 = Peon('w', 6, 7, "pieces/icons8-peón-48 (1).png")
        piecesforLogic[31] = self.white_pawn8
        #--------------------White Empire-----------------------------

    def putPiecesOnBoard(self): #Saca las piezas del vector y los
        global piecesforLogic
        for i in range(0, len(piecesforLogic)):
            #if (piecesforLogic[i] != '*'):
            cx=piecesforLogic[i].getCoordX()
            cy=piecesforLogic[i].getCoordY()
            self.board[cx][cy] = piecesforLogic[i]

    def savePosition(self, pieza):
        coords = [0,0]
        coords[0] = pieza.getCoordX()
        coords[1] = pieza.getCoordY()
        return coords

    def gameTest(self):
        global piecesforLogic
        lastCoords = []
        lastCoords = self.savePosition(piecesforLogic[4])
        piecesforLogic[4].setCoordX(2)
        piecesforLogic[4].setCoordY(2)
        self.board[lastCoords[0]][lastCoords[1]] = '*'


    def printPieces(self):
        print(piecesforLogic)
    def printBoard(self):
        print(self.board)



if __name__ == '__main__':

    gboard = logicChessBoard()

    gboard.drawBoard()
    print("=====================================")
    gboard.loadPieces()
    #gboard.printPieces()
    print("=====================================")
    gboard.putPiecesOnBoard()
    gboard.printBoard()
    print("=====================================")
    gboard.gameTest()
    gboard.printBoard()
    

