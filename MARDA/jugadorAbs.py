from abc import ABCMeta, abstractmethod

class JugadorAbs(metaclass=ABCMeta):
    """
    Clase Jugador Abstracto:
        Es el jugador que actualmente esta en su turno.
    """
    @abstractmethod
    def getName(self):
        """
        :return: Nombre del jugador
        """
        pass
