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

    def __init__():
        self.logic_board = ''
        self.referee = ''
        self.inicio = ''

    @abstractmethod
    def new_window(self):
        pass
   
    @abstractmethod
    def no_names(self):
        pass

    @abstractmethod
    def piece_clicked(self, event):
        pass
        
    @abstractmethod
    def button_click(self):
        pass
        
    @abstractmethod
    def button_quit(self):
        pass	
    
