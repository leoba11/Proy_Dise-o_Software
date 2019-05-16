from tkinter import *


class VentanaInicial(Frame):

	# Builder of the class
    def __init__(self):
        super().__init__()

        self.initUI()

	# Subrotuine that "builds" all the labels and boxes needed to 
	# load the player's name
    def initUI(self):

        self.master.title("Ajedrez Diseño de Software")
        self.pack(fill=BOTH, expand=True)

        frame1 = Frame(self)
        frame1.pack(fill=X)

		# Creates the first label with the Entry box for the white pieces player
        lbl1 = Label(frame1, text="Jugador con fichas blancas:", width=25, fg="white",font=("Helvetica", 16))
        lbl1.pack(side=LEFT, padx=10, pady=50)

        entry1 = Entry(frame1, width=20, bg="white", justify = CENTER, font=("Helvetica", 16)).pack(fill=X, padx=5, pady=50, expand=False)
        
        # PARA EXPANDIR LA COSA CONFORME AGRANDO LA VENTANA
        #entry1.pack(fill=X, padx=5, expand=True)
        
        frame2 = Frame(self)
        
        frame2.pack(fill=X)

        lbl2 = Label(frame2, text="Jugador con fichas negras:", width=25, font=("Helvetica", 16))
        lbl2.pack(side=LEFT, padx=10, pady=15)

        entry2 = Entry(frame2, width=20, bg="white", justify = CENTER, font=("Helvetica", 16)).pack(fill=X, padx=5, pady=40, expand=False)
        
        #buttonPlay = Button(frame2, text="Jugar!!", bd=5, justify=CENTER, width=25, font=("Helvetica", 16)).pack(fill=X, padx=5, pady=40)        
        #buttonPlay.pack(padx=10, pady=15)

def main():

    root = Tk()
    root.geometry("600x300+650+300")
    app = VentanaInicial()
    root.mainloop()


if __name__ == '__main__':
    main()
