import tkinter as tk
#from genRules import *

import PIL.Image
import PIL.ImageTk

class chessRules():

    def __init__(self, master):
        #genericRules.__init__(self, textType, game)
        self.master = master
        self.frame = tk.Frame(self.master)
        self.iconPath1 = 'images/che.jpg'

        text1 = tk.Text(self.frame, height=39, width=67)
        im = PIL.Image.open(self.iconPath1)
        im = im.resize((536,662))
        photo = PIL.ImageTk.PhotoImage(im)
        photo.image = photo
        text1.image_create(tk.END, image=photo)
        text1.pack(side=tk.LEFT)

        text2 = tk.Text(self.frame, height=39, width=67)
        scroll = tk.Scrollbar(self.frame, command=text2.yview)
        text2.configure(yscrollcommand=scroll.set)
        text2.tag_configure('bold_italics', font=('Arial', 10, 'italic'))
        text2.tag_configure('big', foreground='#30730A', font=('Verdana', 15, 'bold'))
        text2.tag_configure('color', foreground='#000000', font=('Tempus Sans ITC', 12, 'bold'))

        #Texto de las reglas basicas del juego
        text2.insert(tk.END,'Reglas Basicas\n', 'big')
        quote = """
El ajedrez es un juego de dos jugadores, donde a un ju-
gador se le asignan piezas blancas y al otro negras. Cada 
jugador dispone de 16 piezas al empezar el juego: un rey, 
una dama o reina, dos torres, dos alfiles, dos caballos y 
ocho peones.  
        """
        text2.insert(tk.END, quote, 'color')

        #Texto del proposito del juego
        text2.insert(tk.END,' \nEl propósito del juego\n', 'big')
        quote1 = """
El objetivo del juego es capturar al rey del otro jugador. 
La captura no se completa nuca, pero una vez que el rey 
es atacado y no puede escapar de esa captura, se dice que es un jaque mate y el juego finaliza.   
        """
        text2.insert(tk.END, quote1, 'color')

        #Texto del inicio del juego
        text2.insert(tk.END,' \nEl comienzo del juego\n', 'big')
        quote1 = """
El juego comienza en la posición que se muestra abajo 
sobre el tablero de ajedrez consistente en 64 casillas en 
una cuadrícula de 8x8. Las blancas (el jugador con las pie-
zas más claras) hacen el primer movimiento. Después ca-
da jugador tiene un único turno para mover. De echo, un 
jugador solo debe hacer un movimiento en cada turno. 
En otras palabras, no se puede saltar el turno para mover.   
        """
        text2.insert(tk.END, quote1, 'color')
         
        self.iconPath = 'images/ima2.png'   

        im2 = PIL.Image.open(self.iconPath)
        im2 = im2.resize((200,200))
        self.icon = PIL.ImageTk.PhotoImage(im2)
        self.icon.image = self.icon  # <== this is were we anchor the img object
        text2.image_create(tk.END, image=self.icon)

        text2.insert(tk.END, '\n')

        #Texto de jugando la partida
        text2.insert(tk.END,' \nJugando la partida\n', 'big')
        quote2 = """
Un movimiento consiste en colocar una pieza en una casilla
diferente, siguiendo las reglas de movimiento de cada pie-
za. Un jugador puede capturar una pieza de su oponente 
moviendo una pieza suya a la casilla en la que está la pie-
za de su oponente. La pieza del oponente se retira del ta-
blero y permanecerá fuera de juego el resto de la partida.   
        """
        text2.insert(tk.END, quote2, 'color')

        #Texto de jaque
        text2.insert(tk.END,' \nJaque\n', 'big')
        quote2 = """
Si un rey es amenazado de que va a ser capturado, pero 
tieneposibilidades de escapar, se dice jaque. Un rey no 
puede moverse donde se le vaya a hacer jaque, y si se en-
cuentra en jaque se debe mover inmediatamente fuera de 
jaque hay tres maneras en las que debes moverte fuera 
de jaque: 

            • Capturando la pieza que ha hecho el jaque.
     
            • Bloqueando la línea de ataque colocando tus 
                propias piezas entre la pieza que ha hecho ja-
                que y tu rey (Por supuesto, un rey no puede ser 
                bloqueado).
     
            • Moviendo el rey fuera de la zona de jaque.
        """
        text2.insert(tk.END, quote2, 'color')

        #Texto de Jaque Mate
        text2.insert(tk.END,' \nJaque Mate\n', 'big')
        quote3 = """
El principal objetivo en el ajedrez en hacer jaque mate al
rey de tu oponente. Cuando un rey no puede evitar ser 
capturado se dice que es jaque mate y el juego finaliza in-
mediatamente.
        """
        text2.insert(tk.END, quote3, 'color')

        #Texto de Tablas por ahogado
        text2.insert(tk.END,' \nTablas de ahogado\n', 'big')
        quote4 = """
Se dice 'tablas' cuando al jugador que le toca mover no 
puede hacer ningún movimiento legal y su rey no esta en 
jaque. Esto finaliza inmediatamente el juego.
        """
        text2.insert(tk.END, quote4, 'color')

        text2.pack(side=tk.LEFT)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
       
        self.frame.pack()
