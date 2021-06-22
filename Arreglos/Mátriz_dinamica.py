A=[[2,5],[1,0,5],[1,1,7],[1,0,3],[2,1,0],[2,1,1]]


n=A[0][0]
C=A[0][1]
d=[]
lastAnswere=0
lastAnsweres=[]
#así se crea una mátriz dinamica
for i in range(n):
    d.append([])
idx=0


#clono desde la segunda fila hasta abajo
Ab=A[1:][:]




#asi se puede recorrer una matriz asimetrica
for i in range(len(Ab)):
    for j in range(len(Ab[i])):
        if Ab[i][0]==1 and j==0:
            idx=((Ab[i][1] ^ lastAnswere)%n)
            d[idx].append(Ab[i][2])


        if Ab[i][0]==2 and j==0:
            idx=((Ab[i][1] ^ lastAnswere)%n)
            idx2=(Ab[i][2]%len(d[idx]))
            lastAnswere=d[idx][idx2]
            lastAnsweres.append(lastAnswere)







