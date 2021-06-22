import  itertools

# nota para este ejercicio, leer mejor la entrada pues en el arreglo tambien estaba tomando el tamaño del arreglo como
#elemento

#Ej: en 2 5 4 sacaba un arreglo de [2,5,4] y debio de ser 2 el tamaño y [5,4] el arreglo

In= list(map(int,input().rstrip().split()))
n=[]
N=[]
for _ in range(In[0]):
    n = list(map(int, input().rstrip().split()))[1:]
    N.append(n)

Pc = list(itertools.product(*N)) # tambien peudo mandar a llamar todos los elementos así

Maximiza=0
for k in range(len(Pc)):
    if Maximiza < sum(map(lambda x:x**2,Pc[k]))%In[1]:
        Maximiza = sum(map(lambda x:x**2,Pc[k]))%In[1]

print(Maximiza)






"""
o puede ser este las dos  son validas


import  itertools


In= list(map(int,input().rstrip().split()))[1:]
n=[]
N=[]
s='list(itertools.product('
for a in range(In[0]):
    n = list(map(int, input().rstrip().split()))
    N.append(n)
    if a+1 == In[0]:
        s = s + f'N[{a}]))'

    else:
        s = s+f'N[{a}],'

Pc = eval(s)

Maximiza=0
for k in range(len(Pc)):
    if Maximiza < sum(list(map(lambda x:x**2,Pc[k]))) % In[1]:
        print(Pc[k])
        Maximiza = sum(list(map(lambda x:x**2,Pc[k]))) % In[1]
        print(Maximiza)






ENTRADA

3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 

>>206


6 767
2 488512261 423332742
2 625040505 443232774
1 4553600
4 92134264 617699202 124100179 337650738
2 778493847 932097163
5 489894997 496724555 693361712 935903331 518538304

>>763

"""


