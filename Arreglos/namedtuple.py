
from collections import namedtuple

x = int(input())
Prom = namedtuple('Prom', input())
#aqui puede recibir los datos tal cual los agarra para que le asigne nombre a cada  capo

print(sum([int(Prom(*input().split()).MARKS) for _ in range(x)])/x)
# creamos una lista que suma todo los promedios y los divide entre x
#pero lo interezante es  *input().split() ya que con esto recive todos los valores en esa linea
# y los asigna a su resprectivo campo
#esto solo funciona solo no los named tuple(no lo he visto en otro lado)


"""
Más detalles de lo anterior ejecutar este codigo
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
from collections import namedtuple

x = int(input())
Prom = namedtuple('Prom', input())
Prom1 = Prom(*input().split())
print(Prom1)

>>Prom(ID='1', MARKS='97', NAME='Raymond', CLASS='7')
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Entrada
5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6
"""