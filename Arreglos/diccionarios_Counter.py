from collections import Counter

input()
Az = Counter(map(int, input().rstrip().split()))

# podemos modificar el valor del diccionario apuntando con la llave -> Az[2] = 0  decimos que a la llave con
#  valor 2 le asignamos 0

Total = 0
for _ in range(int(input())):
    Talla, Pago = map(int, input().split())
    if Az[Talla]==0:
        continue
    else:
        Az[Talla]=Az[Talla]-1 # buscamos por la llave y le asignamos el nuevo valor pero decrementado
        Total += Pago

print(Total)

"""
ENTRADA

10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

SALIDA

200 # pago total

"""
