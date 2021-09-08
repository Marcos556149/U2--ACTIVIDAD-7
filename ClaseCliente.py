class Cliente:
    __tiempo = 0
    __numero=0
    def __init__(self,time):
        self.__tiempo = time
    def setNumero(self,xnum):
        self.__numero = xnum
    def getNumero(self):
        return self.__numero
    def getTiempo(self):
        return int(self.__tiempo)
