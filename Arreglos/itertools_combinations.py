from itertools import combinations

CONV = []
conv = input().split()
for i in range(int(conv[1])):
    Lconv = list(combinations(conv[0],i+1)) # scamos todas las combinaciones desde 1 hasta n
    for j in Lconv:
        j= list(j)
        j.sort()                #Ordenamos dentro de la tupla en orden alfabetico en caso de que el tamaño sea mayor a 1
        CONV.append(''.join(j)) # agregamos las combinaciones como cadenas a una lista
CONV.sort() # ordenamos la lista

for k in range(int(conv[1])): # imprimimos primero los de tamaño 1 luego los de 2 y asi hasta n
    for l in CONV:
        if len(l)==k+1:
            print(l)

"""
Se tiene que imprimir todas las posibles cominaciones en orden alfabetico 

//////////
ENTRADA
////////
HACK 2

//////
SALIDA
/////
A
C
H
K
AC
AH
AK
CH
CK
HK
"""

