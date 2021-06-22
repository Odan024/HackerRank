import numpy

n,m = map(int,input().split())

A = numpy.array([input().split() for i in range(n)],dtype=int) # otra manera de llenar una matriz de nxm dimenciones

Sum= numpy.sum(A, axis = 0)

print(numpy.product(Sum))

"""
ENTRADA
2 2
1 2
3 4

SALIDA

24
"""