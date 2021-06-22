from itertools import combinations_with_replacement

CONV = []

per = input().split()

cwr = list(combinations_with_replacement(per[0], int(per[1])))

for j in cwr:
    j = list(j)
    j.sort()  # Ordenamos dentro de la tupla en orden alfabetico en caso de que el tamaño sea mayor a 1
    CONV.append(''.join(j))  # agregamos las combinaciones como cadenas a una lista
CONV.sort()  # ordenamos la lista

print(CONV)

for i in CONV:
    print(''.join(i))

"""
HACK 2
"""



