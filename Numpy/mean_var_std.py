import numpy

n,m = map(int,input().split())

A = numpy.array([input().split() for i in range(n)],dtype=int) # otra manera de llenar una matriz de nxm dimenciones

print(numpy.mean(A,axis=1))
print(numpy.var(A,axis=0))
Std = numpy.std(A)
print(Std.round(11))
"""
ENTRADA
2 2
1 2
3 4

SALIDA
[1.5 3.5]
[1. 1.]
1.11803398875
"""