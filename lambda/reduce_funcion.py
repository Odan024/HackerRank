from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda a,b : a*b,fracs) # multiplica todo un arreglo con Fraciones dentro y da el resultado de la mul
                                       # de todas  ellas
    return t.numerator, t.denominator   # asi se pueden mandar a llamr por partes

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)


"""
3
1 2
3 4
10 6
"""