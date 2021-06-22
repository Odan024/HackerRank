input()

set1= set(map(int,input().rstrip().split()))

for _ in range(int(input())):
    instru = input().split()
    if len(instru)==1:
        # aqui guarda el pop y evalua la cadena como si fuara una linea de codigo
        #                 |
        #                 V
        eval(f'set1.{instru[0]}()') # asi damos un comando que seria set1.pop() pero usamos eval y la variable que
                                    # contenia ese valor dado por consola por f formar (f'...')

    else:
        eval(f'set1.{instru[0]}(int({instru[1]}))')

print(sum(set1))



"""
Entrada
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5

SALIDA

4   # suma de todos los elemento que quedaron despues de las instrucciones


"""
