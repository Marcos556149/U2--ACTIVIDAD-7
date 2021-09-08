from ClaseNodo import Nodo
class Cola:
    __cant=0
    __pr=None
    __ul=None
    def __init__(self):
        self.__cant=0
        self.__pr=None
        self.__ul=None
    def vacia(self):
        return self.__cant == 0
    def insertar(self,x):
        unaCelda= Nodo(x)
        if self.__ul == None:
            self.__pr=unaCelda
        else:
            self.__ul.setSiguiente(unaCelda)
        self.__ul=unaCelda
        self.__cant += 1
        return self.__ul.getDato()
    def suprimir(self):
        if self.vacia():
            print("Cola Vacia")
            return 0
        else:
            aux= self.__pr
            x= self.__pr.getDato()
            self.__pr= self.__pr.getSiguiente()
            self.__cant -= 1
            if self.__pr == None:
                self.__ul= None
            del(aux)
            return x
    def recuperarPrimero(self):
        return self.__pr
    def recorrer(self):
        aux= self.__pr
        while(aux!=None):
            print(aux.getDato())
            aux=aux.getSiguiente()

