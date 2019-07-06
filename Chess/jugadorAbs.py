from abc import ABCMeta, abstractmethod

class JugadorAbs(metaclass=ABCMeta):
    
    @abstractmethod
    def getName(self):
        pass
