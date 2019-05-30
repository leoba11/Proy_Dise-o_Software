from alfil import *
from caballo import *
from peon import *
from reina import *
from rey import *
from torre import *
from chessBoard import *
from tkinter import *

piecesforLogic = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

class logicChessBoard():

    def __init__(self, rows = 8, cols = 8):
        self.rows = rows
        self.cols = cols

    def drawBoard(self):
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
        piecesforLogic[0] = (black_king, (0,4))

        black_queen = Reina('b', 0,3, defPath + "bq.gif")
        piecesforLogic[1] = (black_queen, (0,3))

        black_bishop1 = Alfil('b', 0, 2, defPath + "bb.gif")
        piecesforLogic[2] = (black_bishop1,(0,2))

        black_bishop2 = Alfil('b', 0, 5, defPath + "bb.gif")
        piecesforLogic[3] = (black_bishop2, (0,5))

        black_knigth1 = Caballo('b', 0, 1, defPath + "bn.gif")
        piecesforLogic[4] = (black_knigth1, (0,1))

        black_knigth2 = Caballo('b', 0, 6, defPath + "bn.gif")
        piecesforLogic[5] = (black_knigth2, (0,6))

        black_rook1 = Torre('b', 0, 0, defPath + "br.gif")
        piecesforLogic[6] = (black_rook1, (0,0))

        black_rook2 = Torre('b', 0, 7, defPath + "br.gif")
        piecesforLogic[7] = (black_rook2, (0,7))

        black_pawn1 = Peon('b', 1, 0, defPath + "bp.gif")
        piecesforLogic[8] = (black_pawn1, (1,0))

        black_pawn2 = Peon('b', 1, 1, defPath + "bp.gif")
        piecesforLogic[9] = (black_pawn1, (1,1))

        black_pawn3 = Peon('b', 1, 2, defPath + "bp.gif")
        piecesforLogic[10] = (black_pawn1, (1,2))

        black_pawn4 = Peon('b', 1, 3, defPath + "bp.gif")
        piecesforLogic[11] = (black_pawn1, (1,3))

        black_pawn5 = Peon('b', 1, 4, defPath + "bp.gif")
        piecesforLogic[12] = (black_pawn1, (1,4))

        black_pawn6 = Peon('b', 1, 5, defPath + "bp.gif")
        piecesforLogic[13] = (black_pawn1, (1,5))

        black_pawn7 = Peon('b', 1, 6, defPath + "bp.gif")
        piecesforLogic[14] = (black_pawn1, (1,6))

        black_pawn8 = Peon('b', 1, 7, defPath + "bp.gif")
        piecesforLogic[15] = (black_pawn1, (1,7))
        #--------------------Black Empire-----------------------------
        #--------------------White Empire-----------------------------
        white_king = Rey('w', 7, 4, defPath + "wk.gif")
        piecesforLogic[16] = (white_king, (7,4))

        white_queen = Reina('w', 7,3, defPath + "wq.gif")
        piecesforLogic[17] = (white_queen, (7,3))

        white_bishop1 = Alfil('w', 7, 2, defPath + "wb.gif")
        piecesforLogic[18] = (white_bishop1, (7,2))

        white_bishop2 = Alfil('w', 7, 5, defPath + "wb.gif") 
        piecesforLogic[19] = (white_bishop2, (7,5))

        white_knigth1 = Caballo('w', 7, 1, defPath + "wn.gif")
        piecesforLogic[20] = (white_knigth1, (7,1))

        white_knigth2 = Caballo('w', 7, 6, defPath + "wn.gif")
        piecesforLogic[21] = (white_knigth2, (7,6))

        white_rook1 = Torre('w', 7, 0, defPath + "wr.gif")
        piecesforLogic[22] = (white_rook1, (7,0))

        white_rook2 = Torre('w', 7, 7, defPath + "wr.gif")
        piecesforLogic[23] =  (white_rook2, (7,7))

        white_pawn1 = Peon('w', 6, 0, defPath + "wp.gif")
        piecesforLogic[24] = (white_pawn1, (6,0))

        white_pawn2 = Peon('w', 6, 1, defPath + "wp.gif")
        piecesforLogic[25] = (white_pawn1, (6,1))        

        white_pawn3 = Peon('w', 6, 2, defPath + "wp.gif")
        piecesforLogic[26] = (white_pawn1, (6,2))

        white_pawn4 = Peon('w', 6, 3, defPath + "wp.gif")
        piecesforLogic[27] = (white_pawn1, (6,3))

        white_pawn5 = Peon('w', 6, 4, defPath + "wp.gif")
        piecesforLogic[28] = (white_pawn1, (6,4))

        white_pawn6 = Peon('w', 6, 5, defPath + "wp.gif")
        piecesforLogic[29] = (white_pawn1, (6,5))

        white_pawn7 = Peon('w', 6, 6, defPath + "wp.gif")
        piecesforLogic[30] = (white_pawn1, (6,6))

        white_pawn8 = Peon('w', 6, 7, defPath + "wp.gif")
        piecesforLogic[31] = (white_pawn1, (6,7))
        #--------------------White Empire-----------------------------
        return piecesforLogic

    def prueba(self):
        global piecesforLogic
        print (piecesforLogic[0][1][0])

if __name__ == '__main__':
    board = logicChessBoard()
    print(board.drawBoard())
    print(board.loadPieces())
    print("=====================================")
    board.prueba()

