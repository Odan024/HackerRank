n=int(input()) # numerto de grupos
N = list(map(int, input().rstrip().split()))

x=set()
y=set()

for i in N:
    if i not in x:
        x.add(i)
        y.add(i)
    else:
        y.discard(i)
y= list(y)
print(y[0])

"""
SE tarda mucho pero da la respuesta correcta


n=int(input()) # numerto de grupos
N = list(map(int, input().rstrip().split()))

NS=set(N)# segresa un conjunto pero sin repeticiones por lo que aqui sacamos todos los posibles valores de los subconjuntos

NL=list(NS)


tam=len(NL)
FREC=[]

for i in range(tam):
    if ((N.count(NL[i]))==1):
        R=NL[i]
        break

print(R)

------------------------------------------------------------------------------------------------------------------------
No se tarda pero cuando son más de 100000 datos falla 

from  statistics import mode
n=int(input()) # numerto de grupos
N = list(map(int, input().rstrip().split()))

NS=set(N)# segresa un conjunto pero sin repeticiones por lo que aqui sacamos todos los posibles valores de los subconjuntos

tam=len(N)

tope=tam//n

FIN=[]
FIN1=[]


for i in range(n):
   SCN=set(N[i*tope:(i+1)*tope])#parto la lista en subconjutos y los vielvo set
   FIN.append(list(NS.difference(SCN))) # esos subconjuntos saco la diferencia y los vuelvo a pasar a lista




for i in range(n):
    for j in range(len(FIN[i])):
        FIN1.append(FIN[i][j])

print(mode(FIN1))



"""