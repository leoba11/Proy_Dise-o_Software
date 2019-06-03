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
board = []

class logicChessBoard():

    def __init__(self, rows = 8, cols = 8):
        self.rows = rows
        self.cols = cols

    def drawBoard(self):
        global board
        board = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append("*")
            board.append(row)
        return board

    def loadPieces(self):
        
        root = Tk()
        path = os.getcwd()
        defPath = path + "/images/"
        imgs = os.listdir(defPath)
        global piecesforLogic

        #--------------------Black Empire-----------------------------
        black_king = Rey('b', 0, 4, defPath + "bk.gif")
        piecesforLogic[0] = (black_king.__class__.__name__, (0,4))

        black_queen = Reina('b', 0,3, defPath + "bq.gif")
        piecesforLogic[1] = (black_queen.__class__.__name__, (0,3))

        black_bishop1 = Alfil('b', 0, 2, defPath + "bb.gif")
        piecesforLogic[2] = (black_bishop1.__class__.__name__,(0,2))

        black_bishop2 = Alfil('b', 0, 5, defPath + "bb.gif")
        piecesforLogic[3] = (black_bishop2.__class__.__name__, (0,5))

        black_knigth1 = Caballo('b', 0, 1, defPath + "bn.gif")
        piecesforLogic[4] = (black_knigth1.__class__.__name__, (0,1))

        black_knigth2 = Caballo('b', 0, 6, defPath + "bn.gif")
        piecesforLogic[5] = (black_knigth2.__class__.__name__, (0,6))

        black_rook1 = Torre('b', 0, 0, defPath + "br.gif")
        piecesforLogic[6] = (black_rook1.__class__.__name__, (0,0))

        black_rook2 = Torre('b', 0, 7, defPath + "br.gif")
        piecesforLogic[7] = (black_rook2.__class__.__name__, (0,7))

        black_pawn1 = Peon('b', 1, 0, defPath + "bp.gif")
        piecesforLogic[8] = (black_pawn1.__class__.__name__, (1,0))

        black_pawn2 = Peon('b', 1, 1, defPath + "bp.gif")
        piecesforLogic[9] = (black_pawn2.__class__.__name__, (1,1))

        black_pawn3 = Peon('b', 1, 2, defPath + "bp.gif")
        piecesforLogic[10] = (black_pawn3.__class__.__name__, (1,2))

        black_pawn4 = Peon('b', 1, 3, defPath + "bp.gif")
        piecesforLogic[11] = (black_pawn4.__class__.__name__, (1,3))

        black_pawn5 = Peon('b', 1, 4, defPath + "bp.gif")
        piecesforLogic[12] = (black_pawn5.__class__.__name__, (1,4))

        black_pawn6 = Peon('b', 1, 5, defPath + "bp.gif")
        piecesforLogic[13] = (black_pawn6.__class__.__name__, (1,5))

        black_pawn7 = Peon('b', 1, 6, defPath + "bp.gif")
        piecesforLogic[14] = (black_pawn7.__class__.__name__, (1,6))

        black_pawn8 = Peon('b', 1, 7, defPath + "bp.gif")
        piecesforLogic[15] = (black_pawn8.__class__.__name__, (1,7))
        #--------------------Black Empire-----------------------------
        #--------------------White Empire-----------------------------
        white_king = Rey('w', 7, 4, defPath + "wk.gif")
        piecesforLogic[16] = (white_king.__class__.__name__, (7,4))

        white_queen = Reina('w', 7,3, defPath + "wq.gif")
        piecesforLogic[17] = (white_queen.__class__.__name__, (7,3))

        white_bishop1 = Alfil('w', 7, 2, defPath + "wb.gif")
        piecesforLogic[18] = (white_bishop1.__class__.__name__, (7,2))

        white_bishop2 = Alfil('w', 7, 5, defPath + "wb.gif") 
        piecesforLogic[19] = (white_bishop2.__class__.__name__, (7,5))

        white_knigth1 = Caballo('w', 7, 1, defPath + "wn.gif")
        piecesforLogic[20] = (white_knigth1.__class__.__name__, (7,1))

        white_knigth2 = Caballo('w', 7, 6, defPath + "wn.gif")
        piecesforLogic[21] = (white_knigth2.__class__.__name__, (7,6))

        white_rook1 = Torre('w', 7, 0, defPath + "wr.gif")
        piecesforLogic[22] = (white_rook1.__class__.__name__, (7,0))

        white_rook2 = Torre('w', 7, 7, defPath + "wr.gif")
        piecesforLogic[23] =  (white_rook2.__class__.__name__, (7,7))

        white_pawn1 = Peon('w', 6, 0, defPath + "wp.gif")
        piecesforLogic[24] = (white_pawn1.__class__.__name__, (6,0))

        white_pawn2 = Peon('w', 6, 1, defPath + "wp.gif")
        piecesforLogic[25] = (white_pawn2.__class__.__name__, (6,1))        

        white_pawn3 = Peon('w', 6, 2, defPath + "wp.gif")
        piecesforLogic[26] = (white_pawn3.__class__.__name__, (6,2))

        white_pawn4 = Peon('w', 6, 3, defPath + "wp.gif")
        piecesforLogic[27] = (white_pawn4.__class__.__name__, (6,3))

        white_pawn5 = Peon('w', 6, 4, defPath + "wp.gif")
        piecesforLogic[28] = (white_pawn5.__class__.__name__, (6,4))

        white_pawn6 = Peon('w', 6, 5, defPath + "wp.gif")
        piecesforLogic[29] = (white_pawn6.__class__.__name__, (6,5))

        white_pawn7 = Peon('w', 6, 6, defPath + "wp.gif")
        piecesforLogic[30] = (white_pawn7.__class__.__name__, (6,6))

        white_pawn8 = Peon('w', 6, 7, defPath + "wp.gif")
        piecesforLogic[31] = (white_pawn8.__class__.__name__, (6,7))
        #--------------------White Empire-----------------------------
        return piecesforLogic

    def putPiecesOnBoard(self): #Saca las piezas del vector y los
        global piecesforLogic
        global board 
        board = self.drawBoard()

        for i in range(0, len(piecesforLogic)):
            cx=piecesforLogic[i][1][0]
            cy=piecesforLogic[i][1][1]
            board[cx][cy] = piecesforLogic[i]
        
        return board

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
        global board
        for i in range(0, len(piecesforLogic)):
            cx=piecesforLogic[i][1][0]
            cy=piecesforLogic[i][1][1]
            board[cx][cy] = piecesforLogic[i]

if __name__ == '__main__':
    gboard = logicChessBoard()

    print(gboard.loadPieces())
    print("=====================================")
    print(gboard.putPiecesOnBoard())
    print("=====================================")

    #gboard.prueba()
    gboard.game()
    #print(gboard.refresh())

