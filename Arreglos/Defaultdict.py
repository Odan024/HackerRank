from collections import defaultdict

n, m = map(int, input().split())

D = defaultdict(list) # decimos que contendra listas por default si no se le asigna un valor

for i in range(n+m):
    if i+1 <=n:
        D['A'].append(input().rstrip()) # asiganmos los valores pasados
    else:
        D['B'].append(input().rstrip())

print(D)
Impr = []

for i in range(len(D['B'])): # le decimos que tendra el tamaño de la lista que contiene esa llave
    if D['B'][i] in D['A']:  # Dict[llave][indice_lista]
        for j in range(len(D['A'])):
            if D['A'][j] == D['B'][i]: # asi se pregunta por los indices de ambas listas, lo podriamos ver como un arreglo bidimencional
                Impr.append(str(j+1))
    else:
        Impr.append('-1')


    print(' '.join(Impr))
    Impr.clear()



"""
STDIN   Function
-----   --------
5 2     group A size n = 5, group B size m = 2
a       group A contains 'a', 'a', 'b', 'a', 'b'
a
b
a
b
a       group B contains 'a', 'b'
b

ENTRADA

5 2     
a       
a
b
a
b
a       
b


SALIDA

1 2 4  # indice de a que se repiten en b 
3 5

"""