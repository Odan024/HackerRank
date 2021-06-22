from itertools import product

a = list(map(int,input().rstrip().split()))
b = list(map(int,input().rstrip().split()))

convina = list(product(a,b))

for i in convina:
    print(i ,end=" ")

"""


1 2 #a
3 4 #b

devuelve el producto cartesioano entre 2 listas 

>>(1, 3) (1, 4) (2, 3) (2, 4)

"""