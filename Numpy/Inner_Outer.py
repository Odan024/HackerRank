import numpy

M1 = (list(map(int, input().rstrip().split())))
M2 = (list(map(int, input().rstrip().split())))

numpy.array(M1)
numpy.array(M2)

print(numpy.inner(M1, M2))
print(numpy.outer(M1, M2))

"""
0 1
2 3
"""