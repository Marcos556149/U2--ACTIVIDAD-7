class Nodo:
    __dato=0
    __sig=None
    def __init__(self,dat):
        self.__dato=dat
        self.__sig=None
    def getSiguiente(self):
        return self.__sig
    def setSiguiente(self,siguiente):
        self.__sig=siguiente
    def getDato(self):
        return self.__dato
    def setDato(self,dat):
        self.__dato=dat 
