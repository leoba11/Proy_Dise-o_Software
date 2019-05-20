from tkinter import *
from tkinter import messagebox
import time

class VentanaGuardar(Frame):

    # Builder of the class
    def __init__(self, master):
        super().__init__()

        self.master.title("Ajedrez Diseno de Software")
        self.pack()

        # Creates the button to submit the players names
        self.buttonLoad = Button(master, text="Cargar Partida", bg="green", bd=5, justify=CENTER, width=15, font=("Helvetica", 16), command=self.button_load)
        self.buttonLoad.place(relx=0.65, rely=0.40)

        self.buttonSave = Button(master, text="Guardar Partida", bg="blue", bd=5, justify=CENTER, width=15, font=("Helvetica",16), command=self.button_save)
        self.buttonSave.place(relx=0.10, rely=0.40)

        self.buttonLoad = Button(master, text="Salir", bg="red", bd=5, justify=CENTER, width=10, font=("Helvetica", 16), command=self.button_quit)
        self.buttonLoad.place(relx=0.40, rely=0.80)

    # Subroutine that extracts the players names and stores them into the class attributes
    def button_load(self):
        pass

    def button_save(self):
        pass

    # Subroutine that closes the complete window
    def button_quit(self):
        self.quit()


def main():
    root = Tk()
    root.geometry("600x300")
    app = VentanaGuardar(root)#.pack()
    root.mainloop()

if __name__ == '__main__':
    main()
