import numpy

M = numpy.array(list(map(int,input().rstrip().split())),dtype=int)
print(numpy.reshape(M,(3,3)))

"""
ENTRADA

1 2 3 4 5 6 7 8 9

SALIDA

[[1 2 3]
 [4 5 6]
 [7 8 9]]



"""