from jugadorAbs import *

class Jugador(JugadorAbs):
	
	# Constructor of the player
    def __init__(self, name):
        
        self.name = name
        
    # Method that returns the player's name
    def getName(self):
        
        return self.name
