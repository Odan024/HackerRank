#listas enlaszadas
Names=[]
Scores=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    Names.append(name)
    Scores.append(score)

print(Names)
print(Scores)
Ord=[]
NomOrd=[]
second=1
for i in range(len(Scores)):


    a=Scores.index(min(Scores))
    A=Scores.pop(a)#remueve el indice de el valor mas pequeño y regresa su valor
    B=Names.pop(a)
    if second == 2:
            if A in Ord:
                Ord.append(A)
                NomOrd.append(B)


            else:
                break

    if len(Ord)== 0:
        Ord.append(A)
    if second < 2 and i>0:
        if A in Ord:
            Ord.append(A)
        else:
            second+=1
            Ord.clear()
            Ord.append(A)
            NomOrd.append(B)

print()

print(Ord)
print(NomOrd)
print()

NomOrd.sort()
for i in range(len(NomOrd)):
    print(NomOrd[i])



"""
A= Scores.index(min(Scores))
print(A)
print(Scores)
Scores.remove(Scores[A])
Names.remove(Names[A])"""