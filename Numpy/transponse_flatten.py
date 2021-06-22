import numpy

N, M = map(int,input().rstrip().split())

# manera eficiente de llenar los datos de un numpy array con listas de comprension
#recuerda que la estructura de un numpy.array es numpy.array([]) dentro la lista que queremos cambiar a numpy.array
#aprovechamos esa lista para llenar los datos

M1 = numpy.array([numpy.array(input().split(),dtype=int) for i in range(N)])

print(numpy.transpose(M1))
print(M1.flatten())


"""
ENTRADA

2 2
1 2
3 4

SALIDA

[[1 3]
 [2 4]]
[1 2 3 4]
"""