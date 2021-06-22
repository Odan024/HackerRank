import numpy

# se puede hacer más de una asignacion  todo se asigna de detecha a izquierda
# 1° mapeamos un array introducido en consola y a su vez este se tranforma en un numpy.array de flotantes
# 2° invertimos la numpy.array
# 3° a la array ya invertida la asignamos a M

M = M[::-1] = numpy.array(list(map(int, input().rstrip().split())), dtype=float)
print(M)

"""
ENTRADA
1 2 3 4 -8 -10

SALIDA
[-10.  -8.   4.   3.   2.   1.]
"""
