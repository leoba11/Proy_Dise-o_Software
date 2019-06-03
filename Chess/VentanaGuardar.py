from tkinter import *
from tkinter import messagebox
import time
from logicChessBoard import *

class VentanaGuardar(Frame):

    # Builder of the class
    def __init__(self, master):
        super().__init__()
        #self.piecesforLogic = logicChessBoard.piecesforLogic
        self.piecesforLogic = ["pieza",(1,2),"kefnse",(2,1),"efe",(3,7)]

        self.master.title("Ajedrez Diseno de Software")
        self.pack()

        # Creates the button to submit the players names
        self.buttonLoad = Button(master, text="Cargar Partida", bg="green", bd=5, justify=CENTER, width=15, font=("Helvetica", 16), command=self.button_load)
        self.buttonLoad.place(relx=0.65, rely=0.40)

        self.buttonSave = Button(master, text="Guardar Partida", bg="blue", bd=5, justify=CENTER, width=15, font=("Helvetica",16), command=self.button_save(self.piecesforLogic))
        self.buttonSave.place(relx=0.10, rely=0.40)

        self.buttonLoad = Button(master, text="Salir", bg="red", bd=5, justify=CENTER, width=10, font=("Helvetica", 16), command=self.button_quit)
        self.buttonLoad.place(relx=0.40, rely=0.80)

    # Subroutina a la que le llega el vector un piezas de Tablero y se encarga de guardarlo en un .csv
    def button_load(self):
        pass


    # Subroutina que e encarga de leer de un .csv a un vector de piezas que luego se le pasa a Tablero para que las coloque
    def button_save(self,piecesforLogic):
        f = open("saveFile.txt", "w+")
        for element in piecesforLogic:
            s = str(element)
            f.write(s + "\n")

        f.close()


    def button_quit(self):
        self.quit()


def main():
    root = Tk()
    root.geometry("600x300")
    app = VentanaGuardar(root)
    root.mainloop()

if __name__ == '__main__':
    main()
