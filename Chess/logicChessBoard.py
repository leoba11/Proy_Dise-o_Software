from alfil import *
from caballo import *
from peon import *
from reina import *
from rey import *
from torre import *
from chessBoard import *
from tkinter import *
from tkinter import messagebox

#Se inicializa en 0's para evitar problemas
#Variables globales
piecesforLogic = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 


class logicChessBoard():

    def __init__(self, rows = 8, cols = 8):
        self.board = []
        self.rows = rows
        self.cols = cols
        
        # Variable to control who is the next player (first white pieces)
        self.next_player = 'w'
        
        # Variables to control who is the king that can be threatened
        self.potential_king_killed = 'b'
        self.potential_king_name = 'bk'
        
        # Creates a king piece for comparing later 
        self.rey_prueba = Rey('k', 'r', 0, 10, "pieces/icons8-rey-48.png")
        
        # Variables to control the positions of the two kings
        self.posX_bk = 0
        self.posY_bk = 4
        
        self.posX_wk = 7
        self.posY_wk = 4
        
        self.drawBoard()
        self.loadPieces()
        self.putPiecesOnBoard()
        #self.gameTest()
        
        
    # Function that returns the next player color
    def getNextPlayer(self):
        return self.next_player
        
    def refreshBoard(self):
        print("entré=============================")
        global piecesforLogic
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if not self.board[i][j] == '*':
                    piecesforLogic[i] = self.board[i][j]
                    
                    
		
	# Subroutine that changes or switches the next player and the king that can be
	# threatened
    def changeNextPlayer(self):
		
        if (self.next_player == 'w'):
            self.next_player = 'b'
            self.potential_king_killed = 'w'
            self.potential_king_name = 'wk'
        else:
            self.next_player = 'w'
            self.potential_king_killed = 'b'
            self.potential_king_name = 'bk'
            
            
            
    # Creates a list of all the possible moves of all the pieces in the current play
    def getAttackMoves(self):
        attack_moves = []
        piece_moves = []
		
		# Traverses all the board in order to check the possible moves
        for i in range(self.rows):
            for j in range(self.cols):
				
                if (self.board[i][j] != '*'):
                    if (self.board[i][j].getColor() == self.next_player):
						
                        piece_moves = self.board[i][j].canMove(self)
						# Adds the potential moves of the piece into the final list
                        attack_moves.extend(piece_moves)
                        piece_moves.clear()
		
        return attack_moves
    
    
    # Function that checks if the king
    def checkPieceKing(self, coord_x, coord_y):
        
        if (type(self.board[coord_x][coord_y]) == type(self.rey_prueba)):
            self.setPositionKing(self.board[coord_x][coord_y].getColor(), coord_x, coord_y)
    
    
    # Function that returns a tuple with the coordinates of the king threatened
    def returnPositionsKingThreatened(self):
        if (self.potential_king_killed == 'b'):
            return (self.posX_bk, self.posY_bk)
        else:
            return (self.posX_wk, self.posY_wk)
            
            
            
    # Function that sets a tuple for the king MOVED by the user
    def setPositionKing(self, color, coord_x, coord_y):
        if (color == 'b'):
            self.posX_bk = coord_x
            self.posY_bk = coord_y
        else:
            self.posX_wk = coord_x
            self.posY_wk = coord_y
            
            
    
    # Checks if one of the kings is threatened for check-mate
    def isPotentialCheckMate(self, attack_moves):

        isCheckMate = True
        
        # Stores the name pieces for the board
        name_pieces = 'blancas' if (self.potential_king_killed == 'b') else 'negras'
        name_pieces_losing = 'negras' if (self.potential_king_killed == 'b') else 'blancas'
        
        # Gets the coords of the king
        coords_king = self.returnPositionsKingThreatened() 
        
        if (coords_king in (attack_moves)):

            moves_king = self.board[coords_king[0]][coords_king[1]].canMove(self)
            
            # Checks if the king can move to escape from the check mate
            for i in range(len(moves_king)):
                
                if (not ( moves_king[i] in (attack_moves))):
                    isCheckMate = False						# Escapes from the check mate
			
            if (isCheckMate):
                messagebox.showinfo("GANADOR!","JAQUE MATE! Ganaron las piezas " + name_pieces)
            else:
                messagebox.showwarning("CUIDADO!", "Piezas " + name_pieces_losing + " en jaque")
		

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
    
    
    # Function that checks if the square or field requested for the player is empty
    def isEmpty(self, coordX, coordY):
        #print (coordX, coordY)
        if (coordX < 0  or coordX > 7 or coordY < 0 or coordY > 7):
            return False
        else:
            if(self.board[coordX][coordY] == '*'):#type(14)):
                return True
            else:
                return False


    # Function that checks if on the square requested for the player is occupied by the enemy
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
        #root = Tk()
        global piecesforLogic

        #--------------------Black Empire-----------------------------
        self.black_king = Rey("bk",'b', 0, 4, "pieces/icons8-rey-48.png")
        #print("HI")
        #print(type(self.black_king))
        piecesforLogic[0] = self.black_king
        #self.board[0][4] = self.black_king

        self.black_queen = Reina("bq",'b', 0,3, "pieces/icons8-reina-48.png")
        #self.board[0][3] = self.black_queen
        piecesforLogic[1] = self.black_queen
        #piecesforLogic[1] = '*'

        self.black_bishop1 = Alfil("bbl",'b', 0, 2, "pieces/icons8-obispo-48.png")
        #self.board[0][2] = self.black_bishop1
        piecesforLogic[2] = self.black_bishop1
        #piecesforLogic[2] = '*'

        self.black_bishop2 = Alfil("bbr",'b', 0, 5, "pieces/icons8-obispo-48.png")
        #self.board[0][5] = self.black_bishop2
        piecesforLogic[3] = self.black_bishop2
        #piecesforLogic[3] = '*'

        self.black_knight1 = Caballo("bnl",'b', 0, 1, "pieces/icons8-caballero-48.png")
        #self.board[0][1] = self.black_knight1
        piecesforLogic[4] = self.black_knight1
        #piecesforLogic[4] = '*'

        self.black_knight2 = Caballo("bnr",'b', 0, 6, "pieces/icons8-caballero-48.png")
        #self.board[0][6] = self.black_knight2
        piecesforLogic[5] = self.black_knight2
        #piecesforLogic[5] = '*'

        self.black_rook1 = Torre("brl",'b', 0, 0, "pieces/icons8-torre-48.png")
        #self.board[0][0] = self.black_rook1
        piecesforLogic[6] = self.black_rook1

        self.black_rook2 = Torre("brr",'b', 0, 7, "pieces/icons8-torre-48.png")
        #self.board[0][7] = self.black_rook2
        piecesforLogic[7] = self.black_rook2

        self.black_pawn1 = Peon("bp",'b', 1, 0, "pieces/icons8-peón-48.png")
        #self.board[1][0] = self.black_pawn1
        piecesforLogic[8] = self.black_pawn1

        self.black_pawn2 = Peon("bp1",'b', 1, 1, "pieces/icons8-peón-48.png")
        #self.board[1][1] = self.black_pawn2
        piecesforLogic[9] = self.black_pawn2

        self.black_pawn3 = Peon("bp2",'b', 1, 2, "pieces/icons8-peón-48.png")
        #self.board[1][2] = self.black_pawn3
        piecesforLogic[10] = self.black_pawn3

        self.black_pawn4 = Peon("bp3",'b', 1, 3, "pieces/icons8-peón-48.png")
        #self.board[1][3] = self.black_pawn4
        piecesforLogic[11] = self.black_pawn4
        #piecesforLogic[11] = '*'

        self.black_pawn5 = Peon("bp4",'b', 1, 4, "pieces/icons8-peón-48.png")
        #self.board[1][4] = self.black_pawn5
        piecesforLogic[12] = self.black_pawn5
        #piecesforLogic[12] = '*'

        self.black_pawn6 = Peon("bp5",'b', 1, 5, "pieces/icons8-peón-48.png")
        #self.board[1][5] = self.black_pawn6
        piecesforLogic[13] = self.black_pawn6
        #piecesforLogic[13] = '*'

        self.black_pawn7 = Peon("bp6",'b', 1, 6, "pieces/icons8-peón-48.png")
        #self.board[1][6] = self.black_pawn7
        piecesforLogic[14] = self.black_pawn7

        self.black_pawn8 = Peon("bp7",'b', 1, 7, "pieces/icons8-peón-48.png")
        #self.board[1][7] = self.black_pawn8
        piecesforLogic[15] = self.black_pawn8
        #piecesforLogic[15] = '*'
        #--------------------Black Empire-----------------------------
        #--------------------White Empire-----------------------------
        self.white_king = Rey("wk",'w', 7, 4, "pieces/icons8-rey-48 (1).png")
        #self.board[7][4] = self.white_king
        piecesforLogic[16] = self.white_king

        self.white_queen = Reina("wq",'w', 7,3, "pieces/icons8-reina-48 (1).png")
        #self.board[7][3] = self.white_queen
        piecesforLogic[17] = self.white_queen

        self.white_bishop1 = Alfil("wbl",'w', 7, 2, "pieces/icons8-obispo-48 (1).png")
        #self.board[7][2] = self.white_bishop1
        piecesforLogic[18] = self.white_bishop1

        self.white_bishop2 = Alfil("wbr",'w', 7, 5, "pieces/icons8-obispo-48 (1).png") 
        #self.board[7][5] = self.white_bishop2
        piecesforLogic[19] = self.white_bishop2

        self.white_knight1 = Caballo("wnl",'w', 7, 1, "pieces/icons8-caballero-48 (1).png")
        #self.board[7][1] = self.white_knight1
        piecesforLogic[20] = self.white_knight1

        self.white_knight2 = Caballo("wnr",'w', 7, 6, "pieces/icons8-caballero-48 (1).png")
        #self.board[7][6] = self.white_knight2
        piecesforLogic[21] = self.white_knight2

        self.white_rook1 = Torre("wrl",'w', 7, 0, "pieces/icons8-torre-48 (1).png")
        #self.board[7][0] = self.white_rook1
        piecesforLogic[22] = self.white_rook1

        self.white_rook2 = Torre("wrr",'w', 7, 7, "pieces/icons8-torre-48 (1).png")
        #self.board[7][7] = self.white_rook2
        piecesforLogic[23] = self.white_rook2

        self.white_pawn1 = Peon("wp",'w', 6, 0, "pieces/icons8-peón-48 (1).png")
        #self.board[6][0] = self.white_pawn1
        piecesforLogic[24] = self.white_pawn1

        self.white_pawn2 = Peon("wp1",'w', 6, 1, "pieces/icons8-peón-48 (1).png")
        #self.board[6][1] = self.white_pawn2
        piecesforLogic[25] = self.white_pawn2

        self.white_pawn3 = Peon("wp2",'w', 6, 2, "pieces/icons8-peón-48 (1).png")
        #self.board[6][2] = self.white_pawn3
        piecesforLogic[26] = self.white_pawn3

        self.white_pawn4 = Peon("wp3",'w', 6, 3, "pieces/icons8-peón-48 (1).png")
        #self.board[6][3] = self.white_pawn4
        piecesforLogic[27] = self.white_pawn4

        self.white_pawn5 = Peon("wp4",'w', 6, 4, "pieces/icons8-peón-48 (1).png")
        #self.board[6][4] = self.white_pawn5
        piecesforLogic[28] = self.white_pawn5

        self.white_pawn6 = Peon("wp5",'w', 6, 5, "pieces/icons8-peón-48 (1).png")
        #self.board[6][5] = self.white_pawn6
        piecesforLogic[29] = self.white_pawn6

        self.white_pawn7 = Peon("wp6",'w', 6, 6, "pieces/icons8-peón-48 (1).png")
        #self.board[6][6] = self.white_pawn7
        piecesforLogic[30] = self.white_pawn7

        self.white_pawn8 = Peon("wp7",'w', 6, 7, "pieces/icons8-peón-48 (1).png")
        #self.board[6][7] = self.white_pawn8
        piecesforLogic[31] = self.white_pawn8
        #--------------------White Empire-----------------------------

    def putPiecesOnBoard(self): #Saca las piezas del vector y los
        global piecesforLogic
        for i in range(0, len(piecesforLogic)):
            if (piecesforLogic[i] != '*'):
                cx=piecesforLogic[i].getCoordX()
                cy=piecesforLogic[i].getCoordY()
                self.board[cx][cy] = piecesforLogic[i]

    def savePosition(self, pieza):
        coords = [0,0]
        coords[0] = pieza.getCoordX()
        coords[1] = pieza.getCoordY()
        return coords

    def gameTest(self):
        lastCoords = []
        lastCoords = self.savePosition(piecesforLogic[4])
        piecesforLogic[4].setCoordX(2)
        piecesforLogic[4].setCoordY(2)
        piecesforLogic[3] = '*'
        self.board[lastCoords[0]][lastCoords[1]] = '*'
        self.refresh()
        
        
    
    def logicEat(self, ate): #may need a translater
        global piecesforLogic
        for piece in piecesforLogic:
            if ate == piece.getName():
                print(piece.getName())
                break
        piecesforLogic.remove(piece.getName())
        
        

    def piecesRefresh(self):
        global piecesforLogic
        for i in range(0, len(piecesforLogic)):
            if (piecesforLogic[i] != '*'):
                cx=piecesforLogic[i].getCoordX()
                cy=piecesforLogic[i].getCoordY()
            self.board[cx][cy] = piecesforLogic[i]
    '''
    def refreshBoard(self):
        global piecesforLogic
        #contador = 0
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if not self.board[i][j] == '*':
                    #contador += 1 
                    #print("Encontré una pieza", contador)
                    piecesforLogic[i] = self.board[i][j]
    '''
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
    #gboard.putPiecesOnBoard()
    gboard.printBoard()
    print("=====================================")
    gboard.gameTest()
    gboard.printBoard()
    

