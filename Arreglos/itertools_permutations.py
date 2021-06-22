from itertools import permutations

per = input().split()

Lper = list(permutations(per[0],int(per[1])))

Lper.sort()

for i in Lper:
    print(''.join(i))

"""
Da todas las permutaciones en orden alfabetico

//////////
ENTRADA
//////////
HACK 2



//////
SALIDA
/////
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
"""