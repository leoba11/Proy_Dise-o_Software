from alfil import *
from caballo import *
from peon import *
from reina import *
from rey import *
from torre import *
from chessBoard import *
from tkinter import *

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
        piecesforLogic = []
        
        path = os.getcwd()
        defPath = path + "/images/"
        imgs = os.listdir(defPath)

        self.black_king = Rey('b', 0, 4, defPath + "bk.gif")
        piecesforLogic[0] = (black_king, (0,4))

        self.black_queen = Reina('b', 0,3, defPath + "bq.gif")
        piecesforLogic[1] = (black_queen, (0,3))


        return self.piecesforLogic
        '''
        black_bishop1 = Alfil('b', 0, 2, defPath + "bb.gif")
        black_bishop1.image.image = black_bishop1.image
        self.addPiece("bbr", black_bishop1.image, black_bishop1.getCoordX(), black_bishop1.getCoordY())
        black_bishop2 = Alfil('b', 0, 5, defPath + "bb.gif")
        black_bishop2.image.image = black_bishop2.image
        self.addPiece("bbl", black_bishop2.image, black_bishop2.getCoordX(), black_bishop2.getCoordY())
        black_knigth1 = Caballo('b', 0, 1, defPath + "bn.gif")
        black_knigth1.image.image = black_knigth1.image
        self.addPiece("bnr", black_knigth1.image, black_knigth1.getCoordX(), black_knigth1.getCoordY())
        black_knigth2 = Caballo('b', 0, 6, defPath + "bn.gif")
        black_knigth2.image.image = black_knigth2.image
        self.addPiece("bnl", black_knigth2.image, black_knigth2.getCoordX(), black_knigth2.getCoordY())
        black_rook1 = Torre('b', 0, 0, defPath + "br.gif")
        black_rook1.image.image = black_rook1.image
        self.addPiece("brr", black_rook1.image, black_rook1.getCoordX(), black_rook1.getCoordY())
        black_rook2 = Torre('b', 0, 7, defPath + "br.gif")
        black_rook2.image.image = black_rook2.image
        self.addPiece("brl", black_rook2.image, black_rook2.getCoordX(), black_rook2.getCoordY())
        black_pawn1 = Peon('b', 1, 0, defPath + "bp.gif")
        black_pawn1.image.image = black_pawn1.image
        self.addPiece("bp0", black_pawn1.image, black_pawn1.getCoordX(), black_pawn1.getCoordY())
        black_pawn2 = Peon('b', 1, 1, defPath + "bp.gif")
        black_pawn2.image.image = black_pawn2.image
        self.addPiece("bp1", black_pawn2.image, black_pawn2.getCoordX(), black_pawn2.getCoordY())
        black_pawn3 = Peon('b', 1, 2, defPath + "bp.gif")
        black_pawn3.image.image = black_pawn3.image
        self.addPiece("bp2", black_pawn3.image, black_pawn3.getCoordX(), black_pawn3.getCoordY())
        black_pawn4 = Peon('b', 1, 3, defPath + "bp.gif")
        black_pawn4.image.image = black_pawn4.image
        self.addPiece("bp3", black_pawn4.image, black_pawn4.getCoordX(), black_pawn4.getCoordY())
        black_pawn5 = Peon('b', 1, 4, defPath + "bp.gif")
        black_pawn5.image.image = black_pawn5.image
        self.addPiece("bp4", black_pawn5.image, black_pawn5.getCoordX(), black_pawn5.getCoordY())
        black_pawn6 = Peon('b', 1, 5, defPath + "bp.gif")
        black_pawn6.image.image = black_pawn6.image
        self.addPiece("bp5", black_pawn6.image, black_pawn6.getCoordX(), black_pawn6.getCoordY())
        black_pawn7 = Peon('b', 1, 6, defPath + "bp.gif")
        black_pawn7.image.image = black_pawn7.image
        self.addPiece("bp6", black_pawn7.image, black_pawn7.getCoordX(), black_pawn7.getCoordY())
        black_pawn8 = Peon('b', 1, 7, defPath + "bp.gif")
        black_pawn8.image.image = black_pawn8.image
        self.addPiece("bp7", black_pawn8.image, black_pawn8.getCoordX(), black_pawn8.getCoordY())
        
        
        # Creates all the white pieces and draws them into the board
        white_king = Rey('w', 7, 4, defPath + "wk.gif")
        white_king.image.image = white_king.image
        self.addPiece("wk", white_king.image, white_king.getCoordX(), white_king.getCoordY())
        white_queen = Reina('w', 7,3, defPath + "wq.gif")
        white_queen.image.image = white_queen.image
        self.addPiece("wq", white_queen.image, white_queen.getCoordX(), white_queen.getCoordY())
        white_bishop1 = Alfil('w', 7, 2, defPath + "wb.gif")
        white_bishop1.image.image = white_bishop1.image
        self.addPiece("wbl", white_bishop1.image, white_bishop1.getCoordX(), white_bishop1.getCoordY())
        white_bishop2 = Alfil('w', 7, 5, defPath + "wb.gif")
        white_bishop2.image.image = white_bishop2.image
        self.addPiece("wbr", white_bishop2.image, white_bishop2.getCoordX(), white_bishop2.getCoordY())
        white_knigth1 = Caballo('w', 7, 1, defPath + "wn.gif")
        white_knigth1.image.image = white_knigth1.image
        self.addPiece("wnl", white_knigth1.image, white_knigth1.getCoordX(), white_knigth1.getCoordY())
        white_knigth2 = Caballo('w', 7, 6, defPath + "wn.gif")
        white_knigth2.image.image = white_knigth2.image
        self.addPiece("wnr", white_knigth2.image, white_knigth2.getCoordX(), white_knigth2.getCoordY())
        white_rook1 = Torre('w', 7, 0, defPath + "wr.gif")
        white_rook1.image.image = white_rook1.image
        self.addPiece("wrl", white_rook1.image, white_rook1.getCoordX(), white_rook1.getCoordY())
        white_rook2 = Torre('w', 7, 7, defPath + "wr.gif")
        white_rook2.image.image = white_rook2.image
        self.addPiece("wrr", white_rook2.image, white_rook2.getCoordX(), white_rook2.getCoordY())
        white_pawn1 = Peon('w', 6, 0, defPath + "wp.gif")
        white_pawn1.image.image = white_pawn1.image
        self.addPiece("wp0", white_pawn1.image, white_pawn1.getCoordX(), white_pawn1.getCoordY())
        white_pawn2 = Peon('w', 6, 1, defPath + "wp.gif")
        white_pawn2.image.image = white_pawn2.image
        self.addPiece("wp1", white_pawn2.image, white_pawn2.getCoordX(), white_pawn2.getCoordY())
        white_pawn3 = Peon('w', 6, 2, defPath + "wp.gif")
        white_pawn3.image.image = white_pawn3.image
        self.addPiece("wp2", white_pawn3.image, white_pawn3.getCoordX(), white_pawn3.getCoordY())
        white_pawn4 = Peon('w', 6, 3, defPath + "wp.gif")
        white_pawn4.image.image = white_pawn4.image
        self.addPiece("wp3", white_pawn4.image, white_pawn4.getCoordX(), white_pawn4.getCoordY())
        white_pawn5 = Peon('w', 6, 4, defPath + "wp.gif")
        white_pawn5.image.image = white_pawn5.image
        self.addPiece("wp4", white_pawn5.image, white_pawn5.getCoordX(), white_pawn5.getCoordY())
        white_pawn6 = Peon('w', 6, 5, defPath + "wp.gif")
        white_pawn6.image.image = white_pawn6.image
        self.addPiece("wp5", white_pawn6.image, white_pawn6.getCoordX(), white_pawn6.getCoordY())
        white_pawn7 = Peon('w', 6, 6, defPath + "wp.gif")
        white_pawn7.image.image = white_pawn7.image
        self.addPiece("wp6", white_pawn7.image, white_pawn7.getCoordX(), white_pawn7.getCoordY())
        white_pawn8 = Peon('w', 6, 7, defPath + "wp.gif")
        white_pawn8.image.image = white_pawn8.image
        self.addPiece("wp7", white_pawn8.image, white_pawn8.getCoordX(), white_pawn8.getCoordY())
        '''
    


if __name__ == '__main__':
    board = logicChessBoard()
    print(board.drawBoard())
    print(board.loadPieces())

