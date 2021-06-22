"""
problema
https://www.hackerrank.com/challenges/find-angle/problem?h_r=next-challenge&h_v=zen

Para la solución de este promeblema partimos el tringulo pequeño en 2 y como un triangulo es exactamente igual al otro
el angulo de C es iguaL al angulo de teta
"""


import math

l1 = int(input())
l2 = int(input())

h = math.hypot(l1,l2)

Ac= round(math.degrees(math.asin(l1/h))) # por sen= co/h


print(f'{Ac}{chr(176)}')

