for i in range(1,int(input())+1): #Optima ya que 1^2 =1, 11^2= 121 , 111^2=12321
    print((pow(10,i)//9)**2)




"""
Entrada
5

SALIDA

1
121
12321
1234321
123454321

------------------------------------------------------------------------------------------------------------------------
Mi forma sin saber que se tenia que resolver en 2 lineas jiji 

n=int(input())
s=''
for i in range(1,n+1):
    for j in range(1,i+1):
        s=s+str(j)

    s2 = s[:-1]
    R = s2[::-1]
    print(s + R)
    s = ''
"""