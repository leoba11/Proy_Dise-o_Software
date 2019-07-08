from abc import ABCMeta, abstractmethod
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


# Clase abstracta que será usada como base para el controlador
class ControllerAbs(metaclass=ABCMeta):
    """
    Clase Controlador Abstracto:
        Es la base de los juegos del MARDA, llama y consturye los ambientes para cada juego.
        Sus atributos son:
            + logic_board
            + referee
            + inicio
    """

    def __init__():
        """
        Construye la clase, con sus atributos antes mencionados.
        """

        self.logic_board = ''
        self.referee = ''
        self.inicio = ''

    @abstractmethod
    def new_window(self):
        """
        Crea una nueva ventana, ya sea la de inicio, la del tablero o la de reglas.
        """
        pass
   
    @abstractmethod
    def no_names(self):
        """
        Verifica que el usuario no haya puesto su nombre a la hora de jugar.
        """
        pass

    @abstractmethod
    def piece_clicked(self, event):
        """
        Ayuda a ver los posibles moviemientos de la pieza clickeada.
        También para moverla.
        """
        pass
        
    @abstractmethod
    def button_click(self):
        """
        Para opciones, de ver reglas o avanzar en el menú de usuarios.
        """
        pass
        
    @abstractmethod
    def button_quit(self):
        """
        Para el botón de salida de la aplicación y de la ventana inicial.
        """
        pass	
    
