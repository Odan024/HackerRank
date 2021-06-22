import numpy

NM=list(map(int,input().rstrip().split()))

#primeramente agrgamos todo comom lista

a=[]
b=[]

for _ in range(NM[0]):
    a.append(list(map(int,input().rstrip().split())))

for _ in range(NM[0]):
    b.append(list(map(int,input().rstrip().split())))

#despues transformamos las matrices en numpy.array

A = numpy.array(a,dtype=int)
B = numpy.array(b,dtype=int)

print(numpy.add(A,B))
print(numpy.subtract(A,B))
print(numpy.multiply(A,B))
print(A//B)
print(numpy.mod(A,B))
print(numpy.power(A,B))



"""
ENTRADA

1 4
1 2 3 4
5 6 7 8

SALIDA

[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]] 

"""



