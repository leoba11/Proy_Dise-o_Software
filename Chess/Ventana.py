from tkinter import *


class VentanaInicial(Frame):

	# Builder of the class
    def __init__(self, master):
        super().__init__()

        self.initUI(master)

	# Subrotuine that "builds" all the labels and boxes needed to 
	# load the player's name
    def initUI(self, master):

        self.master.title("Ajedrez Diseno de Software")
        self.pack()

		# Creates the first label with the Entry box for the white pieces player
        lbl1 = Label(master, text="Jugador con fichas blancas:", width=25, anchor=NW, fg="white",font=("Helvetica", 16))
        
        # places the object in a relative position of the window
        lbl1.place(relx=0.08, rely=0.2)

        entry1 = Entry(master, width=20, bg="white", justify = CENTER, font=("Helvetica", 16))
        entry1.place(relx=0.55, rely=0.2)

        lbl2 = Label(master, text="Jugador con fichas negras:", width=25, anchor=NW, font=("Helvetica", 16))
        lbl2.place(relx=0.08, rely=0.5)

        entry2 = Entry(master, width=20, bg="white", justify = CENTER, font=("Helvetica", 16))
        entry2.place(relx=0.55, rely=0.5)
        
        buttonPlay = Button(master, text="Jugar!!", bg="green", bd=5, justify=CENTER, width=10, font=("Helvetica", 16))
        buttonPlay.place(relx=0.65, rely=0.75)

def main():

    root = Tk()
    root.geometry("600x300+650+300")
    app = VentanaInicial(root).pack()
    root.mainloop()

if __name__ == '__main__':
    main()
