from chessWindow import initialWindow
from chessBoard import chessBoard
from logicChessBoard import logicChessBoard
from chessRules import *
from tkinter import *
from controller import *
import os
import time
import PIL.Image
import PIL.ImageTk

class Referee:
	
    def __init__(self, controller, logic_chessboard):
        
        self.logic_board = logic_chessboard
        
        self.controller = controller
        
        # Variable to control who is the next player (first white pieces)
        self.next_player = 'w'
        
        
    # Function that compares the piece pressed by the user and if the piece is one of the next color to play
    def is_valid_piece(self, coord_x, coord_y):
        if (self.logic_board.board[coord_x][coord_y].getColor() == self.getNextPlayer()):
            return True
        else:
            return False
            
            
    # Function that returns the next player color
    def getNextPlayer(self):
        return self.next_player
       
    
    # Subroutine that changes or switches the next player and the king that can be threatened
    def changeNextPlayer(self):
		
        if (self.next_player == 'w'):
            self.next_player = 'b'
            self.potential_king_killed = 'w'
            self.potential_king_name = 'wk'
        else:
            self.next_player = 'w'
            self.potential_king_killed = 'b'
            self.potential_king_name = 'bk'
            
    
    # Function that checks if the castling move was made by the king
    def checkCastlingMove(self, temp_x, temp_y, coord_x, coord_y):
        
        name = self.logic_board.board[coord_x][coord_y].getName()
        direction = 0
        orientation = 0
        coord_y_tower = 0
        if (name == "wk" or name == "bk"):
            
            # Checks if the king moved two squares
            if ((coord_y == (temp_y - 2))):
                orientation= 1
                direction = -2
                coord_y_tower = (temp_y - 2) + direction
                #Set new tower move
                self.logic_board.changeTowerPosition(direction, orientation, coord_y_tower, coord_x, coord_y)
            else:
                if ((coord_y == (temp_y + 2))):
                    orientation = -1
                    direction = 1
                    coord_y_tower = (temp_y + 2) + direction
                    #Set new tower move
                    self.logic_board.changeTowerPosition(direction, orientation, coord_y_tower, coord_x, coord_y)
                    
                    
                    
     # Checks if one of the kings is threatened for check-mate
    def isPotentialCheckMate(self, attack_moves):

        isCheckMate = True
        
        # Stores the name pieces for the board
        name_pieces = 'blancas' if (self.logic_board.getPotentialKingThreatened() == 'b') else 'negras'
        name_pieces_losing = 'negras' if (self.logic_board.getPotentialKingThreatened() == 'b') else 'blancas'
        
        # Gets the coords of the king
        coords_king = self.logic_board.returnPositionsKingThreatened() 
        
        if (coords_king in (attack_moves)):

            moves_king = self.logic_board.board[coords_king[0]][coords_king[1]].canMove(self.logic_board)
            
            # Checks if the king can move to escape from the check mate
            for i in range(len(moves_king)):
                
                if (not ( moves_king[i] in (attack_moves))):
                    isCheckMate = False						# Escapes from the check mate
			
            if (isCheckMate):
                messagebox.showinfo("FIN DE JUEGO!","JAQUE MATE! Ganaron las piezas " + name_pieces)
            else:
                messagebox.showwarning("CUIDADO!", "Piezas " + name_pieces_losing + " en jaque")
                
                
    # Creates a list of all the possible moves of all the pieces in the current play
    def getAttackMoves(self):
        attack_moves = []
        piece_moves = []
		
		# Traverses all the board in order to check the possible moves
        for i in range(self.logic_board.rows):
            for j in range(self.logic_board.cols):
				
                if (self.logic_board.board[i][j] != '*'):
                    if (self.logic_board.board[i][j].getColor() == self.next_player):
						
                        piece_moves = self.logic_board.board[i][j].canMove(self.logic_board)
						# Adds the potential moves of the piece into the final list
                        attack_moves.extend(piece_moves)
                        piece_moves.clear()
		
        return attack_moves
