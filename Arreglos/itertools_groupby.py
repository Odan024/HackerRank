from itertools import groupby

s = input()



for key, group in groupby(s): # se itera sobre 2, sobre la llave y sobre el grupo
    a = len(list(group)),int(key)
    print(tuple(a), end=" ")


"""
////////
ENTRADA
///////
1222311


///////
SALIDA
//////


(1, 1) (3, 2) (1, 3) (2, 1)   # veces que el numero se repite  y el numero


"""