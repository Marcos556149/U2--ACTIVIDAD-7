from ClaseCajero import Cajero
from ClaseCliente import Cliente
from ClaseCola import Cola
from random import randint
if __name__=='__main__':
    Simulacion= 50
    CajTiempo= int(input("Ingrese el tiempo de atencion del cajero: "))
    CliTiempo=int(input("Ingrese la frecuencia de llegada de los clientes: "))
    unaCola=Cola()
    unCajero= Cajero(CajTiempo)
    llego=None
    libre=None
    cont=1
    maximo=0
    numeroCliente=1
    espera='---'
    print("----COMIENZO DE LA SIMULACION----")
    while cont <= Simulacion:
        random = 1/randint(1,CliTiempo)
        if random==1/CliTiempo:
            unCliente= Cliente(cont)
            unCliente.setNumero(numeroCliente)
            unaCola.insertar(unCliente)
            llego='Cliente {}'.format(numeroCliente)
            numeroCliente += 1
        else:
            llego='---'
        if unCajero.getliberado():
            if unaCola.vacia() == False:
                ClienteCola=unaCola.suprimir()
                espera= cont-ClienteCola.getTiempo()
                if espera > maximo:
                    maximo=espera
                unCajero.setEstado()
                libre='Cajero atiende cliente {}'.format(ClienteCola.getNumero())
            else:
                libre='Libre'
        else:
            libre='Ocupado'
            unCajero.contar()
        print('{0:^20}{1:^20}{2:^20}{3:^20}'.format(cont,llego,libre,espera))
        espera='---'
        cont += 1
        input()
    print("TIEMPO MAXIMO DE ESPERA: ",maximo)







