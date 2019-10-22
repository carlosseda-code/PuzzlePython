''' Juego Puzzle
    Autor: Carlos Seda
    Fecha de creación: 16/10/2019
'''
import random
import sys
def alea():
    '''Función que devuelve una lista de numeros en orden aleatorio con un rango específico''' 
    numeros = list(range(0, 16))
    random.shuffle(numeros)
    return numeros
def salir():
    '''Función para finalizar el juego'''
    print("¡Gracias por jugar!")
    print("¡Gracias por jugar!")
    print("¡Gracias por jugar!")
    sys.exit()    
def muestra_matriz(matriz):
    '''Función para mostrar la matriz y guardar la posición del 0'''
    for ren in range(4):
        for col in range(4):
            if matriz[ren][col]==0:
                print(" ",end="  ")
                ren0 = ren
                col0 = col
            elif matriz[ren][col]>10:
                print(matriz[ren][col],end=" ")
            else:
                print(matriz[ren][col],end="  ")
        print()
    return ren0,col0
def main():
    matriz = []
    n=0
    numero = 0
    print("¡Bienvenido!")
    print("Puzzle: Por Carlos Seda")
    numeros = alea()
    for ren in range (4):
        lista=[]
        for col in range (4):
            if(numeros[n]==0):
                lista.append(0)
            else:
                 lista.append(numeros[n])
            n+=1
        matriz.append(lista)
    ren0,col0 = muestra_matriz(matriz)
    while(numero!=-1):
        numero = input("¿Qué número desea mover? (Teclea -1 para salir del juego)      ")
        try:
            numero = int(numero)
            if numero==-1:
                salir()
            else:
                renglones=len(matriz)
                columnas=len(matriz[0])
                if ren0==renglones-1 and col0==0:
                    if matriz[ren0-1][col0]==numero:
                        matriz[ren0-1][col0] = 0
                        matriz[ren0][col0] = numero
                    elif matriz[ren0][col0+1]==numero:
                        matriz[ren0][col0+1] = 0
                        matriz[ren0][col0] = numero
                    else:
                        print("")
                elif ren0==0 and col0==0:
                    if matriz[ren0][col0+1]==numero:
                        matriz[ren0][col0+1] = 0
                        matriz[ren0][col0] = numero
                    elif matriz[ren0+1][col0]==numero:
                        matriz[ren0+1][col0] = 0
                        matriz[ren0][col0] = numero
                    else:
                        print("No disponible")
                elif col0==0 and ren0<renglones-1 and ren0>0:
                    if matriz[ren0][col0+1]==numero:
                        matriz[ren0][col0+1] = 0
                        matriz[ren0][col0] = numero
                    elif matriz[ren0+1][col0]==numero:
                        matriz[ren0+1][col0] = 0
                        matriz[ren0][col0] = numero
                    elif matriz[ren0-1][col0]==numero:
                        matriz[ren0-1][col0] = 0
                        matriz[ren0][col0] = numero
                    else:
                        print("")
                elif ren0==0 and col0>0 and col0<columnas-1:
                    if matriz[ren0][col0-1]==numero:
                        matriz[ren0][col0-1] = 0
                        matriz[ren0][col0] = numero
                    if matriz[ren0][col0+1]==numero:
                        matriz[ren0][col0+1] = 0
                        matriz[ren0][col0] = numero
                    elif matriz[ren0+1][col0]==numero:
                        matriz[ren0+1][col0] = 0
                        matriz[ren0][col0] = numero
                    else:
                        print("")
                elif col0==columnas-1 and ren0==0:
                    if matriz[ren0][col0-1]==numero:
                        matriz[ren0][col0-1] = 0
                        matriz[ren0][col0] = numero
                    elif matriz[ren0+1][col0]==numero:
                        matriz[ren0+1][col0] = 0
                        matriz[ren0][col0] = numero
                    else:
                        print("")
                elif col0==columnas-1 and ren0>0 and ren0<renglones-1:
                    if matriz[ren0][col0-1]==numero:
                        matriz[ren0][col0-1] = 0
                        matriz[ren0][col0] = numero
                    elif matriz[ren0-1][col0]==numero:
                        matriz[ren0-1][col0] = 0
                        matriz[ren0][col0] = numero
                    elif matriz[ren0+1][col0]==numero:
                        matriz[ren0+1][col0] = 0
                        matriz[ren0][col0] = numero
                    else:
                        print("")
                elif col0==columnas-1 and ren0==renglones-1:
                    if matriz[ren0][col0-1]==numero:
                        matriz[ren0][col0-1] = 0
                        matriz[ren0][col0] = numero
                    elif matriz[ren0-1][col0]==numero:
                        matriz[ren0-1][col0] = 0
                        matriz[ren0][col0] = numero
                    else:
                        print("")
                elif ren0==renglones-1 and col0>0 and col0<columnas-1:
                    if matriz[ren0][col0-1]==numero:
                        matriz[ren0][col0-1] = 0
                        matriz[ren0][col0] = numero
                    elif matriz[ren0][col0+1]==numero:
                        matriz[ren0][col0+1] = 0
                        matriz[ren0][col0] = numero
                    elif matriz[ren0-1][col0]==numero:
                        matriz[ren0-1][col0] = 0
                        matriz[ren0][col0] = numero
                    else:
                        print("")
                else:
                    if matriz[ren0][col0-1]==numero:
                        matriz[ren0][col0-1] = 0
                        matriz[ren0][col0] = numero
                    elif matriz[ren0-1][col0]==numero:
                        matriz[ren0-1][col0] = 0
                        matriz[ren0][col0] = numero
                    elif matriz[ren0][col0+1]==numero:
                        matriz[ren0][col0+1] = 0
                        matriz[ren0][col0] = numero
                    elif matriz[ren0+1][col0]==numero:
                        matriz[ren0+1][col0]=0
                        matriz[ren0][col0] = numero
                    else:
                        print("")
        except ValueError:
            print("Digite un número, no un carácter")
        for ren in range(4):
            for col in range(4):
                if matriz[ren][col]==0:
                    print(" ",end = "  ")
                    ren0 = ren
                    col0 = col
                elif matriz[ren][col]>10:
                    print(matriz[ren][col],end = " ")
                else:
                    print(matriz[ren][col],end = "  ")
            print()
main()

