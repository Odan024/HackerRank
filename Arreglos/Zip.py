# Campuramos 2 datos separados por parantesis recibidos desde consola
n, x = map(int, input().rstrip().split())

# Usamos las listas de comprensio para llenarla con tuplas
Lt = [tuple(map(float, input().rstrip().split())) for i in range(x)]

# Zip solo acepta tuplas asi que le damos tuplas

Com = zip(*Lt)  # Ojo el * es un comodin para decir que se usara TODO lo que contine ese iterable
# *Lt == Lt[0],Lt[1],Lt[2]...Lt[n]

for X in Com: # solo iteramos y realizamos el promedio
    a = sum(X)
    print(round(a / x, 1))

"""

ENTRADA

5 3
89 90 78 93 80
90 91 85 88 86
91 92 83 89 90.5

SALIDA

90.0
91.0
82.0
90.0
85.5

"""
