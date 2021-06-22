x=1
y=1
z=2
n=3
A=[a for a in range(0,x+1) ] # esto es comprension de listas (llenar en una linea)
B=[a for a in range(0,y+1) ]
C=[a for a in range(0,z+1) ]
P=[]
l=0
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            P.append([i,j,k])
r=len(P)

R=[P[i] for i in range(r) if sum(P[i])!=n] #aqui iteramos toda la lista pero le ponemos la condicion de que solo los elementos que sumados no den n

print(A)
print(B)
print(C)
print()
print(P)
print(R)



