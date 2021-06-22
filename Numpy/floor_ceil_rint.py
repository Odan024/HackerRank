import numpy
numpy.set_printoptions(legacy='1.13') # para el espacio entre la impresion

A = numpy.array(input().split(), dtype=float)

print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))




