# from operator import itemgetter

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    #Otra manera seria

    #arr= sorted(arr, key=itemgetter(k)) # con elemento llamable

    arr.sort(key=lambda arr: arr[k]) # podemos dar una llave para que ordene con que valor va a ordenar el arreglo
                                     # de arreglos pero unicamnete key= recibe metodos o elementos llamables
                                     # por eso implementamos un metodo sin nombre (labda)

    print(arr)


    for i in arr:
        print(*i) # imprimir con un *y luego la vaciable solo imprime los datos sin un formato de cadena unicamente
                  #variables

       # 7 1 0   <---- se imprimiria así

      #print(i)   de este modo se imprimirian

      # [7, 1, 0]


"""
Primer intento etsa correcto pero tranformo toda la cadena en str para poder relizar un join e imprimirlo 

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    arr.sort(key=lambda arr: arr[k])

    print(arr)


    for i in range(n):
        for j in range(m):
            arr[i][j]= str(arr[i][j])

    for x in range(n):
        print(' '.join(arr[x]))
        
        
//////////////////////////////////////
ENTRADA
//////////////////////////////////////

5 3     #tamaño de la matriz
10 2 5   #ini Datos
7 1 0
9 9 9
1 23 12
6 5 9   #fin Datos
1       # ordenamiento por la columna 1

"""
