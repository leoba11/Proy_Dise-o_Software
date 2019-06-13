import tkinter as tk
import os
from tkinter import *
from genBoard import *
from caballo import Caballo
from rey import Rey
from reina import Reina
from alfil import Alfil
from torre import Torre
from peon import Peon

from chessRules import *

import PIL.Image
import PIL.ImageTk

class chessBoard(tk.Frame, genBoard): #Hereda de tk y genBoard
    
    def __init__(self, logic_board,rows, columns, color1, color2, size, parent):
        pass
        genBoard.__init__(self, rows, columns, color1, color2)
        self.size = size
        self.pieces = {} #Tener ciudado
        
        self.logic_board = logic_board
        
        # Variable to check if one piece is already clicked
        self.isPieceClicked = False
        self.isPieceAboutDie = False
        
        self.temporarySquares = []
        self.possible_moves = []
        
        #Dimensions
        canvasWidth = columns * size
        canvasHeight = rows * size

        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth = 0, highlightthickness = 0, width = canvasWidth, height = canvasHeight, background = 'bisque')
        
        #self.caballito = Caballo("wnr",'b', 0, 6, "images/bn.gif")
        
        # Relates the mouse clicked to a function called piece_clicked
        self.canvas.bind("<Button-1>", self.piece_clicked)
        
        self.canvas.bind("<ButtonRelease-1>", self.piece_dropped)
        
        self.canvas.pack(side = 'top', fill = 'both', expand = True, padx = 2, pady = 2)

        self.frame = tk.Frame(self)

        self.button1 = tk.Button(self.frame, text = 'Ver Reglas', width = 25, command = self.new_window)
        self.button1.pack()
        self.frame.pack()

        #self.canvas.bind('<Configure>', self.refresh)
        self.refresh()
        
    # Function that compares the piece pressed by the user and if the piece is one of the next color to play
    def is_valid_piece(self, coord_x, coord_y):
        if (self.logic_board.board[coord_x][coord_y].getColor() == self.logic_board.getNextPlayer()):
            return True
        else:
            return False
			
    # Relates the clicked cell of the board to a duple of coordinates
    def piece_clicked(self, event):
        coord_x = int((event.y / self.size))
        coord_y = int((event.x / self.size))
        
        # Checks if the square clicked is a piece and if not other one has been pressed
        if ((not (self.logic_board.isEmpty(coord_x, coord_y))) and (not (self.isPieceClicked)) and (not (self.isPieceAboutDie)) 
            and (self.is_valid_piece(coord_x, coord_y))):
			
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
                    #print(self.possible_moves)
                    x1 = (self.possible_moves[i][1] * self.size)
                    y1 = (self.possible_moves[i][0] * self.size)
                    x2 = x1 + self.size
                    y2 = y1 + self.size	
                    self.canvas.create_rectangle(x1,y1,x2,y2,outline="white", fill="#9C9C9C", tags="square")
                    self.canvas.update_idletasks()
            else:
                self.isPieceClicked = False
                self.isPieceAboutDie = False
        
        else:
			# Checks if the another piece was clicked
            if ( (self.isPieceClicked) and (not (self.isPieceAboutDie)) and (not (self.logic_board.isEmpty(coord_x, coord_y))) 
                and (self.is_valid_piece(self.temporary_pos_x, self.temporary_pos_y)) ):
				
                print("second condition")
                
                # Colors all moves from the anterior piece clicked into its original state
                for j in range(len(self.temporarySquares)):
                    x1 = (self.temporarySquares[j][1] * self.size)
                    y1 = (self.temporarySquares[j][0] * self.size)
                    x2 = x1 + self.size
                    y2 = y1 + self.size
                    summ = self.temporarySquares[j][1] + self.temporarySquares[j][0]
                    color = self.getEvenColor() if (summ % 2 == 0) else self.getOddColor()
                    self.canvas.create_rectangle(x1,y1,x2,y2,outline="white", fill=color, tags="square")
                
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
                    self.canvas.create_rectangle(x1,y1,x2,y2,outline="white", fill="#9C9C9C", tags="square")
                   
                # Refresh the changes on the board
                self.canvas.update_idletasks()
            
            # In case that the user wants to move the piece already clicked
            else:
                if ( (self.isPieceClicked) and (self.isPieceAboutDie) and ( (self.logic_board.isEmpty(coord_x, coord_y) or 
				    (self.logic_board.isEnemy(self.logic_board.board[self.temporary_pos_x][self.temporary_pos_y].getColor(), coord_x, coord_y)  ) ) )
				    and (self.is_valid_piece(self.temporary_pos_x, self.temporary_pos_y)) ):
						
                        print("third condition")
						# Checks if the movement requested by the user is one of the possible moves
                        if ((coord_x, coord_y) in self.possible_moves):

                            self.isPieceClicked = False			# Restart the attribute isPieceClicked
                            self.isPieceAboutDie = False
                            temp_x = self.temporary_pos_x
                            temp_y = self.temporary_pos_y
                            
                            if (self.logic_board.board[coord_x][coord_y] != '*'):
                                self.canvas.delete(self.logic_board.board[coord_x][coord_y].getName())
                            
                            
                            self.logic_board.board[coord_x][coord_y] = self.logic_board.board[temp_x][temp_y]
                            self.logic_board.board[coord_x][coord_y].movePiece((coord_x,coord_y))
                            self.logic_board.board[temp_x][temp_y] = '*' # en la pos de antes ya no está esa pieza


                            eaterPiece = self.getPiece(temp_x,temp_y)
                            print("la pieza que estoy agarrando es: ", eaterPiece)

                            attack_moves = self.logic_board.getAttackMoves()
                            
                            self.logic_board.isPotentialCheckMate(attack_moves)
                            
                            x1 = (temp_y * self.size)
                            y1 = (temp_x * self.size)
                            x2 = x1 + self.size
                            y2 = y1 + self.size
                            summ = temp_x + temp_y
                            color = self.getEvenColor() if (summ % 2 == 0) else self.getOddColor()
                            self.canvas.create_rectangle(x1, y1, x2, y2, outline="white", fill=color, tags="square")
                                                    
                            # Refresh the changes on the board
                            self.canvas.update_idletasks()
                            
                            #print (attack_moves)
                            
                            # Changes the next player 
                            self.logic_board.changeNextPlayer()
                            self.loadInitPosPiece()
                            self.refresh()

        return (coord_x, coord_y)
			
        
    # Relates the dropped cell of the board to a duple of coordinates
    def piece_dropped(self, event):
        coord_x = int((event.y / self.size))
        coord_y = int((event.x / self.size))
        #print ("dropped at", event.x, event.y, coord_x, coord_y)
    
    # Deletes the piece eliminated from the pieces map
    def ded(self, x, y, eaterPiece):
        '''
        for img in self.pieces:
            if (self.pieces[img][0] == x and self.pieces[img][1] == y):
                print(img)
                break
        '''
        del (self.pieces[eaterPiece])
        

    #Agregar nueva ventana
    def new_window(self):
        self.newWindow = tk.Toplevel()
        self.newWindow.title('CHESS RULES')
        self.app = chessRules(self.newWindow)
        #self.refresh(self.refresh)

    #Add a piece to the tab to be used
    def addPiece(self, name, image, row, column):
        self.canvas.create_image(0,0, image = image, tags = name, anchor = 'c')
        self.placePiece(name, row, column)

    def placePiece(self, name, row, column):
        self.pieces[name] = (row, column)
        x0 = (column * self.size) + int(self.size/2)
        y0 = (row * self.size) + int(self.size/2)
        self.canvas.coords(name, x0, y0)
   
    def loadInitPosPiece(self):
        self.pieces.clear()
        counter = 0
        # Checks the entire board
        for i in range(self.rows):
            for j in range(self.columns):      
                # Checks if the square checked has a piece
                if (self.logic_board.board[i][j] != '*'):
                    self.addPiece(self.logic_board.board[i][j].getName(), self.logic_board.board[i][j].getImage(), i, j)
                    counter +=1

    def printPieces(self):
        print(self.pieces)
    
    def refresh(self):
        color = self.color2
        for row in range(self.rows):
            color = self.color1 if color == self.color2 else self.color2
            for col in range(self.columns):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="white", fill=color, tags="square")
                color = self.color1 if color == self.color2 else self.color2
        c = 0
        for name in self.pieces:
            c += 1
            #print(name, c)
            self.placePiece(name, self.pieces[name][0], self.pieces[name][1]) #Add the piece

        self.canvas.tag_raise("piece")
        self.canvas.tag_lower("square")

    def getPiece(self, x, y):
        for img in self.pieces:
            if self.pieces[img][0] == x and self.pieces[img][1] == y:
                return img
