import numpy
M1=[]
M2=[]

n=int(input())


for i in range(n*2): #
    if i<n:
      M1.append(list(map(int, input().rstrip().split()))) #agregamos una lista dentro de otra
    else:
        M2.append(list(map(int, input().rstrip().split())))

numpy.array(M1)
numpy.array(M2)

print(M1)
print(M2)

print(numpy.dot(M1,M2)) # hacemos la multimplicacion de matrices

"""
2
1 2
3 4
1 2
3 5
"""