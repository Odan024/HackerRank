from numpy import zeros,ones,int


instruc = tuple(map(int,input().rstrip().split()))



print(zeros(instruc, dtype = int))

print(ones(instruc, dtype = int))



"""
Entrada
3 3 3

SALIDA 

una matriz de ceros con las dimensione de entarda y una matriz de 1s con las dimenciones de entrada 


---Otro modo con eval---

from numpy import zeros,ones,int


instruc = list(map(int,input().rstrip().split()))

s='('
for a in range(len(instruc)):
    if a+1 == len(instruc):
        s = s + f'instruc[{a}])'

    else:
        s = s+f'instruc[{a}],'


print(zeros(eval(s), dtype = int))

print(ones(eval(s), dtype = int))



"""