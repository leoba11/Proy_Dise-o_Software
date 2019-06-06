from alfil import *
from caballo import *
from peon import *
from reina import *
from rey import *
from torre import *
from chessBoard import *
from tkinter import *

#Se inicializa en 0's para evitar problemas
#Variables globalesda
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

    def drawBoard(self):
        #global board
        #board = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append("*")
            self.board.append(row)
        
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
        path = os.getcwd()
        defPath = path + "/images/"
        imgs = os.listdir(defPath)
        global piecesforLogic

        #--------------------Black Empire-----------------------------
        self.black_king = Rey('b', 0, 4, defPath + "bk.gif")
        piecesforLogic[0] = self.black_king

        #self.black_queen = Reina('b', 0,3, defPath + "bq.gif")
        #piecesforLogic[1] = self.black_queen
        piecesforLogic[1] = '*'

        #self.black_bishop1 = Alfil('b', 0, 2, defPath + "bb.gif")
        #piecesforLogic[2] = self.black_bishop1
        piecesforLogic[2] = '*'

        self.black_bishop2 = Alfil('b', 0, 5, defPath + "bb.gif")
        piecesforLogic[3] = self.black_bishop2
        #piecesforLogic[3] = '*'

        #self.black_knight1 = Caballo('b', 0, 1, defPath + "bn.gif")
        #piecesforLogic[4] = self.black_knight1
        piecesforLogic[4] = '*'

        self.black_knight2 = Caballo('b', 0, 6, defPath + "bn.gif")
        piecesforLogic[5] = self.black_knight2
        #piecesforLogic[5] = '*'

        self.black_rook1 = Torre('b', 0, 0, defPath + "br.gif")
        piecesforLogic[6] = self.black_rook1

        self.black_rook2 = Torre('b', 0, 7, defPath + "br.gif")
        piecesforLogic[7] = self.black_rook2

        self.black_pawn1 = Peon('b', 1, 0, defPath + "bp.gif")
        piecesforLogic[8] = self.black_pawn1

        self.black_pawn2 = Peon('b', 1, 1, defPath + "bp.gif")
        piecesforLogic[9] = self.black_pawn2

        self.black_pawn3 = Peon('b', 1, 2, defPath + "bp.gif")
        piecesforLogic[10] = self.black_pawn3

        self.black_pawn4 = Peon('b', 1, 3, defPath + "bp.gif")
        piecesforLogic[11] = self.black_pawn4
        #piecesforLogic[11] = '*'

        self.black_pawn5 = Peon('b', 1, 4, defPath + "bp.gif")
        piecesforLogic[12] = self.black_pawn5
        #piecesforLogic[12] = '*'

        self.black_pawn6 = Peon('b', 1, 5, defPath + "bp.gif")
        piecesforLogic[13] = self.black_pawn6
        #piecesforLogic[13] = '*'

        self.black_pawn7 = Peon('b', 1, 6, defPath + "bp.gif")
        piecesforLogic[14] = self.black_pawn7

        #self.black_pawn8 = Peon('b', 1, 7, defPath + "bp.gif")
        #piecesforLogic[15] = self.black_pawn8
        piecesforLogic[15] = '*'
        #--------------------Black Empire-----------------------------
        #--------------------White Empire-----------------------------
        self.white_king = Rey('w', 7, 4, defPath + "wk.gif")
        piecesforLogic[16] = self.white_king

        self.white_queen = Reina('w', 7,3, defPath + "wq.gif")
        piecesforLogic[17] = self.white_queen

        self.white_bishop1 = Alfil('w', 7, 2, defPath + "wb.gif")
        piecesforLogic[18] = self.white_bishop1

        self.white_bishop2 = Alfil('w', 7, 5, defPath + "wb.gif") 
        piecesforLogic[19] = self.white_bishop2

        self.white_knight1 = Caballo('w', 7, 1, defPath + "wn.gif")
        piecesforLogic[20] = self.white_knight1

        self.white_knight2 = Caballo('w', 7, 6, defPath + "wn.gif")
        piecesforLogic[21] = self.white_knight2

        self.white_rook1 = Torre('w', 7, 0, defPath + "wr.gif")
        piecesforLogic[22] = self.white_rook1

        self.white_rook2 = Torre('w', 7, 7, defPath + "wr.gif")
        piecesforLogic[23] = self.white_rook2

        self.white_pawn1 = Peon('w', 6, 0, defPath + "wp.gif")
        piecesforLogic[24] = self.white_pawn1

        self.white_pawn2 = Peon('w', 6, 1, defPath + "wp.gif")
        piecesforLogic[25] = self.white_pawn2

        self.white_pawn3 = Peon('w', 6, 2, defPath + "wp.gif")
        piecesforLogic[26] = self.white_pawn3

        self.white_pawn4 = Peon('w', 6, 3, defPath + "wp.gif")
        piecesforLogic[27] = self.white_pawn4

        self.white_pawn5 = Peon('w', 6, 4, defPath + "wp.gif")
        piecesforLogic[28] = self.white_pawn5

        self.white_pawn6 = Peon('w', 6, 5, defPath + "wp.gif")
        piecesforLogic[29] = self.white_pawn6

        self.white_pawn7 = Peon('w', 6, 6, defPath + "wp.gif")
        piecesforLogic[30] = self.white_pawn7

        self.white_pawn8 = Peon('w', 6, 7, defPath + "wp.gif")
        piecesforLogic[31] = self.white_pawn8
        #--------------------White Empire-----------------------------

    def putPiecesOnBoard(self): #Saca las piezas del vector y los
        global piecesforLogic

        for i in range(0, len(piecesforLogic)):
            if (piecesforLogic[i] != '*'):
                cx=piecesforLogic[i].getCoordX()
                cy=piecesforLogic[i].getCoordY()
                self.board[cx][cy] = piecesforLogic[i]

    def game(self):
        global piecesforLogic
        piecesforLogic[0][1][0].append(5)
        piecesforLogic[0][1][0].append(5)
        

    def prueba(self):
        global piecesforLogic
        print("Pimer Campo: ", piecesforLogic[0])
        print("Segundo Campo [0]: ", piecesforLogic[0][0])
        print("Segundo Campo [1]: ", piecesforLogic[0][1])
        #print("tercer Campo [0][0]: ", piecesforLogic[0][0][0]) #no usar
        #print("tercer Campo [0][1]: ", piecesforLogic[0][0][1]) #No usar
        print("tercer Campo [1][0]: ", piecesforLogic[0][1][0])
        print("tercer Campo [1][1]: ", piecesforLogic[0][1][1])

    def refresh(self):
        global piecesforLogic
        #global board
        for i in range(0, len(piecesforLogic)):
            cx=piecesforLogic[i][1][0]
            cy=piecesforLogic[i][1][1]
            self.board[cx][cy] = piecesforLogic[i]

if __name__ == '__main__':
    gboard = logicChessBoard()

    print(gboard.loadPieces())
    print("=====================================")
    print(gboard.putPiecesOnBoard())
    print("=====================================")

    #gboard.prueba()
    gboard.game()
    #print(gboard.refresh())

