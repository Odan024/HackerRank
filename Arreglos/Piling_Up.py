# Proximo desafio   Word Order
from collections import deque


for _ in range(int(input())):
    tam = int(input())
    Deq = deque(map(int, input().rstrip().split()))
    res = 'Yes'
    Prim = Deq[0]
    Ult = Deq[-1]

    for j in range(tam):

        if len(Deq) == 1:
            if Deq[0] > Prim3 and Deq[0] > Ult3:
                res='No'
                break
            else: break

        elif len(Deq) == 2:
            # pude haber validado con solo un caso if (Deq[0] > Prim3) or (Deq[1] > Prim3) pero lo valide para ambos lados
            if (Deq[0] > Prim3 and Deq[0] > Ult3) or (Deq[1] > Prim3 and Deq[1] > Ult3):
                res = 'No'
                break
            else:
                break

        elif len(Deq) == 3:
            Prim3 = Deq[0]
            Ult3 = Deq[-1]

        elif  len(Deq) == 4:
            Prim3 = Deq[0]
            Ult3 = Deq[-1]
            if Prim3 < Deq[1] or Ult3 < Deq[-2]:
                res = 'No'
                break



        if (Ult < Deq[-1] or Prim < Deq[0]):
            res = 'No'
            break

        elif Deq[0] > Deq[-1]:
            Deq.popleft()



        elif Deq[0] < Deq[-1]:
            Deq.pop()



        elif Deq[0] == Deq[-1]:
            Deq.popleft()
            Deq.pop()



    print(res)
    Deq = []


#   print(Deq[1])   # si se puede accer con indices

"""
2
6
4 3 2 1 3 4
3
1 3 2


----------------------
1            
6            
5 5 5 5 5 5  
--------------------
1
6
5 5 2 5 3 5
----------------
1
6
5 3 2 1 6 5
-----------------------
1 
6
6 5 6 4 4 6

"""