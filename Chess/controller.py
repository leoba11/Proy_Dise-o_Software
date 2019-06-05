from chessWindow import initialWindow
from chessBoard import chessBoard
from logicChessBoard import logicChessBoard
from tkinter import *
import PIL.Image
import PIL.ImageTk

root = Tk()
root.geometry("600x300")

class Controller():
	
	# Constructor 
    def __init__(self):
        self.inicio = initialWindow(root)
        self.tablero_logico = logicChessBoard()
        mainloop()
        
    def begin(self):
        #print("hi")
        self.tablero_logico.loadPieces()
        print("=====================================")
        print(self.tablero_logico.putPiecesOnBoard())
        print("=====================================")
        
        # CAMBIAR LO DE LOGIC CHESSBOARD PARA QUE LO QUE INCLUYA EN LA MATRIZ SEAN A HUEVO LAS PIEZAS!
        possible_moves = self.tablero_logico.board[0][6][0].canMove(self, tablero_logico.board,0,6)


if __name__ == '__main__':
	controlador = Controller()
	controlador.begin()
