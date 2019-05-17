from tkinter import *

class VentanaInicial(Frame):
	
    # Variables to store the players names
    playerWhite_name = "" 
    playerBlack_name = ""
	
    # Builder of the class
    def __init__(self, master):
        super().__init__()
        
        self.master.title("Ajedrez Diseno de Software")
        self.pack()

        # Creates the labels with the Entry boxes for the white and black pieces players
        self.lbl1 = Label(master, text="Jugador con fichas blancas:", width=25, anchor=NW, fg="white",font=("Helvetica", 16))
        
        # places the object in a relative position of the window
        self.lbl1.place(relx=0.08, rely=0.2)

        self.entry1 = Entry(master, width=20, bg="white", justify = CENTER, font=("Helvetica", 16))
        self.entry1.place(relx=0.55, rely=0.2)

        self.lbl2 = Label(master, text="Jugador con fichas negras:", width=25, anchor=NW, font=("Helvetica", 16))
        self.lbl2.place(relx=0.08, rely=0.5)

        self.entry2 = Entry(master, width=20, bg="white", justify = CENTER, font=("Helvetica", 16))
        self.entry2.place(relx=0.55, rely=0.5)
        
        # Creates a text box
        self.box = Text(master, width=45, height=4, wrap=WORD, background="white")
        self.box.place(relx=0.10, rely=0.75)
		
        # Creates the button to submit the players names
        self.buttonPlay = Button(master, text="Jugar!!", bg="green", bd=5, justify=CENTER, width=10, font=("Helvetica", 16), command=self.button_click)
        self.buttonPlay.place(relx=0.65, rely=0.75)
        
    # Subroutine that extracts the players names and stores them into the class attributes 
    def button_click(self):
		# stores into the variables of the class the names written names
        playerWhite_name = self.entry1.get()
        playerBlack_name = self.entry2.get()
        self.box.delete(0.0, END)
        self.box.insert(END, playerWhite_name + " juega con fichas blancas")
        self.box.insert(END, " y ")
        self.box.insert(END, playerBlack_name + " juega con fichas negras")
        #print(playerWhite_name)
        #print(playerBlack_name)

def main():
    root = Tk()
    root.geometry("600x300")
    app = VentanaInicial(root)#.pack()
    root.mainloop()

if __name__ == '__main__':
    main()
