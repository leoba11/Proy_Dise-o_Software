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
    
    def __init__(self, logic_board, rows, columns, color1, color2, size, parent, playerWhite_name, playerBlack_name):
        pass
        genBoard.__init__(self, rows, columns, color1, color2)
        self.size = size
        self.pieces = {} #Tener ciudado
        
        self.logic_board = logic_board
        
        # Stores the names of the players
        self.player_white = playerWhite_name
        self.player_black = playerBlack_name
        
        # Stores the counter of pieces lost
        self.lostWhitePieces= [0,0,0,0,0,0]
        self.lostBlackPieces= [0,0,0,0,0,0]
        
        # Variable to check if one piece is already clicked
        self.isPieceClicked = False
        self.isPieceAboutDie = False
        
        self.temporarySquares = []
        self.possible_moves = []
        
        #Dimensions
        canvasWidth = columns * size
        canvasHeight = rows * size

        tk.Frame.__init__(self, parent)
        
        # Creation of canvas, labels and buttons
        self.canvas = tk.Canvas(self, borderwidth = 0, highlightthickness = 0, width = canvasWidth, height = canvasHeight, background = 'bisque')
        self.canvitas = tk.Canvas(self, borderwidth = 1, highlightthickness = 0,width = 400, height = 200, background = 'bisque')
        
        # Relates the mouse clicked to a function called piece_clicked
        self.canvas.bind("<Button-1>", self.piece_clicked)
        self.canvas.bind("<ButtonRelease-1>", self.piece_dropped)
        
        self.button1 = tk.Button(self.canvitas, text = 'Ver Reglas', width = 61, command = self.new_window)
        self.button1.pack(side='bottom', fill='both')
        
        # Creates the string variables related to the counter of pieces lost 
        self.bk_counter = StringVar()
        self.bk_counter.set(str(0))
        self.bq_counter = StringVar()
        self.bq_counter.set(str(0))
        self.bb_counter = StringVar()
        self.bb_counter.set(str(0))
        self.bn_counter = StringVar()
        self.bn_counter.set(str(0))
        self.br_counter = StringVar()
        self.br_counter.set(str(0))
        self.bp_counter = StringVar()
        self.bp_counter.set(str(0))
        
        self.wk_counter = StringVar()
        self.wk_counter.set(str(0))
        self.wq_counter = StringVar()
        self.wq_counter.set(str(0))
        self.wb_counter = StringVar()
        self.wb_counter.set(str(0))
        self.wn_counter = StringVar()
        self.wn_counter.set(str(0))
        self.wr_counter = StringVar()
        self.wr_counter.set(str(0))
        self.wp_counter = StringVar()
        self.wp_counter.set(str(0))
        
        
        # Creates all the labels for showing the user how many pieces has lost
        self.label_player_white = Label(self.canvitas, text=("Piezas perdidas de " + self.player_white + ":"), width=25, anchor=NW, font=("Helvetica", 16), bg='bisque')
        self.label_player_black = Label(self.canvitas, text=("Piezas perdidas de " + self.player_black + ":"), width=25, anchor=NW, font=("Helvetica", 16), bg='bisque')
        
        # ------------------ Black labels and images ------------------------
        self.label_bk_counter = Label(self.canvitas, textvariable=self.bk_counter, font=("Helvetica", 16), bg='bisque')
        self.label_bq_counter = Label(self.canvitas, textvariable=self.bq_counter, font=("Helvetica", 16), bg='bisque')
        self.label_bb_counter = Label(self.canvitas, textvariable=self.bb_counter, font=("Helvetica", 16), bg='bisque')
        self.label_bn_counter = Label(self.canvitas, textvariable=self.bn_counter, font=("Helvetica", 16), bg='bisque')
        self.label_br_counter = Label(self.canvitas, textvariable=self.br_counter, font=("Helvetica", 16), bg='bisque')
        self.label_bp_counter = Label(self.canvitas, textvariable=self.bp_counter, font=("Helvetica", 16), bg='bisque')
        self.imagen_bk = PIL.Image.open("pieces/icons8-rey-48.png")
        self.imagen_bk = PIL.ImageTk.PhotoImage(self.imagen_bk)
        self.imagen_bk.photo = self.imagen_bk
        self.imagen_bq = PIL.Image.open("pieces/icons8-reina-48.png")
        self.imagen_bq = PIL.ImageTk.PhotoImage(self.imagen_bq)
        self.imagen_bq.photo = self.imagen_bq
        self.imagen_bb = PIL.Image.open("pieces/icons8-obispo-48.png")
        self.imagen_bb = PIL.ImageTk.PhotoImage(self.imagen_bb)
        self.imagen_bb.photo = self.imagen_bb
        self.imagen_bn = PIL.Image.open("pieces/icons8-caballero-48.png")
        self.imagen_bn = PIL.ImageTk.PhotoImage(self.imagen_bn)
        self.imagen_bn.photo = self.imagen_bn
        self.imagen_br = PIL.Image.open("pieces/icons8-torre-48.png")
        self.imagen_br = PIL.ImageTk.PhotoImage(self.imagen_br)
        self.imagen_br.photo = self.imagen_br
        self.imagen_bp = PIL.Image.open("pieces/icons8-peón-48.png")
        self.imagen_bp = PIL.ImageTk.PhotoImage(self.imagen_bp)
        self.imagen_bp.photo = self.imagen_bp
        
        self.label_bk_image = Label(self.canvitas, image=self.imagen_bk, bg='bisque')
        self.label_bq_image = Label(self.canvitas, image=self.imagen_bq, bg='bisque')
        self.label_bb_image = Label(self.canvitas, image=self.imagen_bb, bg='bisque')
        self.label_bn_image = Label(self.canvitas, image=self.imagen_bn, bg='bisque')
        self.label_br_image = Label(self.canvitas, image=self.imagen_br, bg='bisque')
        self.label_bp_image = Label(self.canvitas, image=self.imagen_bp, bg='bisque')
        
        
        # ------------------ White labels and images ------------------------
        self.label_wk_counter = Label(self.canvitas, textvariable=self.wk_counter, font=("Helvetica", 16), bg='bisque')
        self.label_wq_counter = Label(self.canvitas, textvariable=self.wq_counter, font=("Helvetica", 16), bg='bisque')
        self.label_wb_counter = Label(self.canvitas, textvariable=self.wb_counter, font=("Helvetica", 16), bg='bisque')
        self.label_wn_counter = Label(self.canvitas, textvariable=self.wn_counter, font=("Helvetica", 16), bg='bisque')
        self.label_wr_counter = Label(self.canvitas, textvariable=self.wr_counter, font=("Helvetica", 16), bg='bisque')
        self.label_wp_counter = Label(self.canvitas, textvariable=self.wp_counter, font=("Helvetica", 16), bg='bisque')
        self.imagen_wk = PIL.Image.open("pieces/icons8-rey-48 (1).png")
        self.imagen_wk = PIL.ImageTk.PhotoImage(self.imagen_wk)
        self.imagen_wk.photo = self.imagen_wk
        self.imagen_wq = PIL.Image.open("pieces/icons8-reina-48 (1).png")
        self.imagen_wq = PIL.ImageTk.PhotoImage(self.imagen_wq)
        self.imagen_wq.photo = self.imagen_wq
        self.imagen_wb = PIL.Image.open("pieces/icons8-obispo-48 (1).png")
        self.imagen_wb = PIL.ImageTk.PhotoImage(self.imagen_wb)
        self.imagen_wb.photo = self.imagen_wb
        self.imagen_wn = PIL.Image.open("pieces/icons8-caballero-48 (1).png")
        self.imagen_wn = PIL.ImageTk.PhotoImage(self.imagen_wn)
        self.imagen_wn.photo = self.imagen_wn
        self.imagen_wr = PIL.Image.open("pieces/icons8-torre-48 (1).png")
        self.imagen_wr = PIL.ImageTk.PhotoImage(self.imagen_wr)
        self.imagen_wr.photo = self.imagen_wr
        self.imagen_wp = PIL.Image.open("pieces/icons8-peón-48 (1).png")
        self.imagen_wp = PIL.ImageTk.PhotoImage(self.imagen_wp)
        self.imagen_wp.photo = self.imagen_wp
        
        self.label_wk_image = Label(self.canvitas, image=self.imagen_wk, bg='bisque')
        self.label_wq_image = Label(self.canvitas, image=self.imagen_wq, bg='bisque')
        self.label_wb_image = Label(self.canvitas, image=self.imagen_wb, bg='bisque')
        self.label_wn_image = Label(self.canvitas, image=self.imagen_wn, bg='bisque')
        self.label_wr_image = Label(self.canvitas, image=self.imagen_wr, bg='bisque')
        self.label_wp_image = Label(self.canvitas, image=self.imagen_wp, bg='bisque')
        
        # Stores or pack everything
        self.canvas.pack(side = 'left', fill = 'both', expand = True, padx = 2, pady = 2)
        self.canvitas.pack(side = 'right', fill = 'both', expand = True, padx = 2, pady = 2)
        
        # Black labels and images
        self.label_bk_counter.place(relx=0.1, rely=0.2)
        self.label_bq_counter.place(relx=0.25, rely=0.2)
        self.label_bb_counter.place(relx=0.4, rely=0.2)
        self.label_bn_counter.place(relx=0.55, rely=0.2)
        self.label_br_counter.place(relx=0.7, rely=0.2)
        self.label_bp_counter.place(relx=0.85, rely=0.2)
        self.label_bk_image.place(relx=0.13, rely=0.18)
        self.label_bq_image.place(relx=0.28, rely=0.18)
        self.label_bb_image.place(relx=0.43, rely=0.18)
        self.label_bn_image.place(relx=0.58, rely=0.18)
        self.label_br_image.place(relx=0.73, rely=0.18)
        self.label_bp_image.place(relx=0.88, rely=0.18)
        self.label_player_black.place(relx=0.1,rely=0.1)
        # White labels and images
        self.label_wk_counter.place(relx=0.1, rely=0.65)
        self.label_wq_counter.place(relx=0.25, rely=0.65)
        self.label_wb_counter.place(relx=0.4, rely=0.65)
        self.label_wn_counter.place(relx=0.55, rely=0.65)
        self.label_wr_counter.place(relx=0.7, rely=0.65)
        self.label_wp_counter.place(relx=0.85, rely=0.65)
        
        self.label_wk_image.place(relx=0.13, rely=0.63)
        self.label_wq_image.place(relx=0.28, rely=0.63)
        self.label_wb_image.place(relx=0.43, rely=0.63)
        self.label_wn_image.place(relx=0.58, rely=0.63)
        self.label_wr_image.place(relx=0.73, rely=0.63)
        self.label_wp_image.place(relx=0.88, rely=0.63)
        self.label_player_white.place(relx=0.1,rely=0.55)
        self.refresh()
        
      
    # Subroutine that makes the change of the counter of pieces lost in the game, depending on the
    # piece that just died
    def change_counter_loses(self, piece_dead_name):
      
        if (piece_dead_name[0] == 'w'):
            
            if (piece_dead_name[1] == 'k'):
                self.lostWhitePieces[0] = self.lostWhitePieces[0] + 1
                self.wk_counter.set(str(self.lostWhitePieces[0]))
                #break
            if (piece_dead_name[1] == 'q'):
                self.lostWhitePieces[1] = self.lostWhitePieces[1] + 1
                self.wq_counter.set(str(self.lostWhitePieces[1]))
                #break
            if (piece_dead_name[1] == 'b'):
                self.lostWhitePieces[2] = self.lostWhitePieces[2] + 1
                self.wb_counter.set(str(self.lostWhitePieces[2]))
                #break
            if (piece_dead_name[1] == 'n'):
                self.lostWhitePieces[3] = self.lostWhitePieces[3] + 1
                self.wn_counter.set(str(self.lostWhitePieces[3]))
                #break
            if (piece_dead_name[1] == 'r'):
                self.lostWhitePieces[4] = self.lostWhitePieces[4] + 1
                self.wr_counter.set(str(self.lostWhitePieces[4]))
                #break
            if (piece_dead_name[1] == 'p'):
                self.lostWhitePieces[5] = self.lostWhitePieces[5] + 1
                self.wp_counter.set(str(self.lostWhitePieces[5]))
                #break
        else:
            if (piece_dead_name[1] == 'k'):
                self.lostBlackPieces[0] = self.lostBlackPieces[0] + 1
                self.bk_counter.set(str(self.lostBlackPieces[0]))
                #break
            if (piece_dead_name[1] == 'q'):
                self.lostBlackPieces[1] = self.lostBlackPieces[1] + 1
                self.bq_counter.set(str(self.lostBlackPieces[1]))
                #break
            if (piece_dead_name[1] == 'b'):
                self.lostBlackPieces[2] = self.lostBlackPieces[2] + 1
                self.bb_counter.set(str(self.lostBlackPieces[2]))
                #break
            if (piece_dead_name[1] == 'n'):
                self.lostBlackPieces[3] = self.lostBlackPieces[3] + 1
                self.bn_counter.set(str(self.lostBlackPieces[3]))
                #break
            if (piece_dead_name[1] == 'r'):
                self.lostBlackPieces[4] = self.lostBlackPieces[4] + 1
                self.br_counter.set(str(self.lostBlackPieces[4]))
                #break
            if (piece_dead_name[1] == 'p'):
                self.lostBlackPieces[5] = self.lostBlackPieces[5] + 1
                self.bp_counter.set(str(self.lostBlackPieces[5]))
                #break
      
      
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
            if ( (not (self.isPieceClicked) and (self.isPieceAboutDie)) and (not (self.logic_board.isEmpty(coord_x, coord_y))) 
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
                
                #self.isPieceClicked = False
                #self.isPieceAboutDie = False
            
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
                                self.change_counter_loses(self.logic_board.board[coord_x][coord_y].getName())
                                self.canvas.delete(self.logic_board.board[coord_x][coord_y].getName())
                            
                            
                            self.logic_board.board[coord_x][coord_y] = self.logic_board.board[temp_x][temp_y]
                            
                            # Checks if castling was made 
                            self.logic_board.checkCastlingMove(temp_x, temp_y, coord_x, coord_y)
                            
                            # Checks if the king was moved 
                            self.logic_board.checkPieceKing(coord_x, coord_y)
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
		
        self.bk_counter.set(str(1))

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
