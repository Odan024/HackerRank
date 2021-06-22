input()

Mat= list(map(int, input().split()))

A = set(map(int, input().split()))
B = set(map(int, input().split()))

Mat = list(Mat)
Felicidad=0

for i in Mat:
    if i in A:
        Felicidad+=1
    if i in B:
        Felicidad-=1
print(Felicidad)



"""
ENTRADA
3 2
1 5 3
3 1
5 7

SALIDA

1
"""