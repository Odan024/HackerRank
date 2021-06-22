import numpy

n,m = map(int,input().split())

A = numpy.array([input().split() for i in range(n)],dtype=int) # otra manera de llenar una matriz de nxm dimenciones

Min= numpy.min(A, axis = 1)

print(numpy.max(Min))

"""
ENTRADA
4 2
2 5
3 7
1 3
4 0

SALIDA

3
"""