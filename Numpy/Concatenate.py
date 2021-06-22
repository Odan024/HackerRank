import numpy

#creamos un vector ya que a este podremos insertar elementos y quietar elemento

M1 = []
M2 = []

N, M ,P = map(int,input().rstrip().split())

for _ in range(N):
    M1.append(list(map(int,input().rstrip().split())))

for _ in range(M):
    M2.append(list(map(int,input().rstrip().split())))

# una vex llenada la matriz lo convertimos a numpy ya que se pueden hacer distintas operaciones excepto agregar y quitar elementos

M1 = numpy.array(M1,dtype=int)
M2 = numpy.array(M2,dtype=int)

print(M1)

print('...........')

print(M2)

print(numpy.concatenate((M1,M2),axis=0))

"""
ENTRADA

4 3 2
1 2
1 2 
1 2
1 2
3 4
3 4
3 4 


SALIDA

[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]]

"""
