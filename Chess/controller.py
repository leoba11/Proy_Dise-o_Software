from chessWindow import initialWindow
from chessBoard import chessBoard
from logicChessBoard import logicChessBoard
from chessRules import *
from referee import *
from tkinter import *
import os
import time
import PIL.Image
import PIL.ImageTk


class Controller():
	
	# Constructor 
    def __init__(self, parent):
        
        # Variables to control the state of the move
        self.pieces = {} #Tener ciudado
        
        # Variable to check if one piece is already clicked
        self.isPieceClicked = False
        self.isPieceAboutDie = False
        
        self.temporarySquares = []
        self.possible_moves = []
        
        self.size = 64
        
        self.parent = parent
        
        # Creates the logic board
        self.logic_board = logicChessBoard()
        
        # Creates the referee
        self.referee = Referee(self, self.logic_board)
        
        # Creates the view of the initial window
        self.inicio = initialWindow(parent, self.logic_board, self)
        
        
        
################### Methods and functions for the Initial Window #################################
        
    # Method that displays the board after the players wrote their names
    def button_click(self):
		
        # stores into the variables of the class the names written names
        self.playerWhite_name = self.inicio.entry1.get()
        self.playerBlack_name = self.inicio.entry2.get()

        # Checks if the players names have been written in order to start the game
        if len(self.playerWhite_name) is 0 or len(self.playerBlack_name) is 0:
            self.no_names()
              
        # Hides this window and shows the board
        time.sleep(1)
        self.parent.withdraw()
        
        # function to show the window
        self.parent.deiconify()
        
        # Creates the view of the board
        board_root = Toplevel(self.parent)
        self.chessView = chessBoard(self.logic_board, 8, 8, "#F3D484", "#A05D06", 64, board_root, self.playerWhite_name, self.playerBlack_name, self)
        self.chessView.pack(side='top', fill='both', expand='true', padx=4, pady=4)
        self.chessView.loadInitPosPiece()
        
    
    # Method that closes all the windows and finishes the program execution
    def button_quit(self):
        self.inicio.quit()


    # Subroutine that shows the error message box to the user
    def no_names(self):
        messagebox.showerror("Error!", "Falta uno o más nombres de jugador")
        
        
        
################### Methods and functions for the Chess View #################################
    
    
    #Adds the chess rules window
    def new_window(self):
        self.newWindow = Toplevel()
        self.newWindow.title('CHESS RULES')
        self.app = chessRules(self.newWindow)
			
			
			
    # Relates the clicked cell of the board to a duple of coordinates
    def piece_clicked(self, event):
		
        coord_x = int((event.y / self.size))
        coord_y = int((event.x / self.size))
        
        # Checks if the square clicked is a piece and if not other one has been pressed
        if ((not (self.logic_board.isEmpty(coord_x, coord_y))) and (not (self.isPieceClicked)) and (not (self.isPieceAboutDie)) 
            and (self.referee.is_valid_piece(coord_x, coord_y))):
			
            print("first condition")
            self.isPieceClicked = True
            self.isPieceAboutDie = True
            
            self.possible_moves = self.logic_board.board[coord_x][coord_y].canMove(self.logic_board)
            
            if (len(self.possible_moves) != 0):
                # Extracts the temporary positions of the piece already clicked
                self.temporary_pos_x = coord_x
                self.temporary_pos_y = coord_y
				
                # Copies all the list from possible moves to the temporary colored
                self.temporarySquares = self.possible_moves[:]
                # Creates the GREY squares
                for i in range(len(self.possible_moves)):
                    x1 = (self.possible_moves[i][1] * self.size)
                    y1 = (self.possible_moves[i][0] * self.size)
                    x2 = x1 + self.size
                    y2 = y1 + self.size	
                    
                    self.chessView.drawRectangle(x1,y1,x2,y2, "#9C9C9C")
                
            else:
                self.isPieceClicked = False
                self.isPieceAboutDie = False
        
        else:
			# Checks if the another piece was clicked
            if ( (not (self.isPieceClicked) and (self.isPieceAboutDie)) and (not (self.logic_board.isEmpty(coord_x, coord_y))) 
                and (self.referee.is_valid_piece(self.temporary_pos_x, self.temporary_pos_y)) ):
				
                print("second condition")
                
                # Colors all moves from the anterior piece clicked into its original state
                for j in range(len(self.temporarySquares)):
                    x1 = (self.temporarySquares[j][1] * self.size)
                    y1 = (self.temporarySquares[j][0] * self.size)
                    x2 = x1 + self.size
                    y2 = y1 + self.size
                    summ = self.temporarySquares[j][1] + self.temporarySquares[j][0]
                    color = self.chessView.getEvenColor() if (summ % 2 == 0) else self.chessView.getOddColor()
                    
                    self.chessView.drawRectangle(x1,y1,x2,y2, color)
                
                del (self.temporarySquares[:])    
                
                possible_moves = self.logic_board.board[coord_x][coord_y].canMove(self.logic_board)
                
                # Changes the next player 
                #self.logic_board.changeNextPlayer()
                
                # Extracts the temporary positions of the piece already clicked
                self.temporary_pos_x = coord_x
                self.temporary_pos_y = coord_y
            
                # Copies all the list from possible moves to the temporary colored
                self.temporarySquares = possible_moves[:]
                self.possible_moves = possible_moves[:]
            
                # Shows the possible moves for the piece 
                for i in range(len(self.possible_moves)):
                    x1 = (possible_moves[i][1] * self.size)
                    y1 = (possible_moves[i][0] * self.size)
                    x2 = x1 + self.size
                    y2 = y1 + self.size
                    
                    self.chessView.drawRectangle(x1,y1,x2,y2, "#9C9C9C")
                   
                #self.isPieceClicked = False
                #self.isPieceAboutDie = False
            
            # In case that the user wants to move the piece already clicked
            else:
                if ( (self.isPieceClicked) and (self.isPieceAboutDie) and ( (self.logic_board.isEmpty(coord_x, coord_y) or 
				    (self.logic_board.isEnemy(self.logic_board.board[self.temporary_pos_x][self.temporary_pos_y].getColor(), coord_x, coord_y)  ) ) )
				    and (self.referee.is_valid_piece(self.temporary_pos_x, self.temporary_pos_y)) ):
						
                        print("third condition")
						# Checks if the movement requested by the user is one of the possible moves
                        if ((coord_x, coord_y) in self.possible_moves):

                            self.isPieceClicked = False			# Restart the attribute isPieceClicked
                            self.isPieceAboutDie = False
                            temp_x = self.temporary_pos_x
                            temp_y = self.temporary_pos_y
                           
                            if (self.logic_board.board[coord_x][coord_y] != '*'):
                                self.chessView.change_counter_loses(self.logic_board.board[coord_x][coord_y].getName())
                                self.chessView.canvas.delete(self.logic_board.board[coord_x][coord_y].getName())
                            
                            
                            self.logic_board.board[coord_x][coord_y] = self.logic_board.board[temp_x][temp_y]

                            
                            # ESTE METODO ESTÁ DANDO PROBLEMAS AL MOVER AL PINCHE REY!! 
                            self.referee.checkCastlingMove(temp_x, temp_y, coord_x, coord_y)
                            
                            # Checks if the king was moved 
                            self.logic_board.checkPieceKing(coord_x, coord_y)
                            self.logic_board.board[coord_x][coord_y].movePiece((coord_x,coord_y))
                            self.logic_board.board[temp_x][temp_y] = '*' # en la pos de antes ya no está esa pieza


                            #eaterPiece = self.getPiece(temp_x,temp_y)
                            #print("la pieza que estoy agarrando es: ", eaterPiece)

                            attack_moves = self.referee.getAttackMoves()
                            
                            self.referee.isPotentialCheckMate(attack_moves)
                            
                            x1 = (temp_y * self.size)
                            y1 = (temp_x * self.size)
                            x2 = x1 + self.size
                            y2 = y1 + self.size
                            summ = temp_x + temp_y
                            color = self.chessView.getEvenColor() if (summ % 2 == 0) else self.chessView.getOddColor()
                            
                            self.chessView.drawRectangle(x1,y1,x2,y2, color)

                            # Changes the next player 
                            self.referee.changeNextPlayer()
                            self.chessView.loadInitPosPiece()
        
        


if __name__ == '__main__':
	
    root = Tk()
    root.geometry("600x300")
    
    # Initialize the controller
    controlador = Controller(parent = root)
    
    root.mainloop()
