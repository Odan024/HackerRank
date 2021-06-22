import numpy  as np

#Evaluar un polinomio con un valor de x dado

poli = list(map(float, input().rstrip().split()))
x=int(input())


print (np.polyval(poli, x) )

"""
1.1 2 3  coeficientes del polinomio 
0       valor de x
"""