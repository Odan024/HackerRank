# Encuentra el determiante
import numpy

x = int(input())
Mat = []
for _ in range(x):
    Mat.append(list(map(float,input().rstrip().split())))

print(numpy.linalg.det(Mat))

"""
2  Dimensión NxN

1.1 1.1   matris   
1.1 1.1
"""