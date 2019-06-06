class genBoard(object):

    #Constructor
    def __init__(self, rows, columns, color1, color2):
        #Posibles cosas a heredar
        self.rows = rows
        self.columns = columns
        self.color1 = color1
        self.color2 = color2

        #Agregar dimensiones o cosas de interfaz

    #Comprueba la pieza
    def addPiece(image):
        print("Add")
        #Agrega una pieza al tablero

    def restartBoard():
        print("restart")

    def saveBoard():
        print("save")

    def loadBoard():
        print("Load")

    def boardType():
        print("Type")
     
    # Retorna el color de la posición par
    def getEvenColor(self):
        return self.color1
        
    # Retorna el color de la posicion impar
    def getOddColor(self):
        return self.color2
