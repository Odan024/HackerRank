x, L1 = input(), list(map(int, input().rstrip().split())) # aqignacion multiple
print(all(i > 0 for i in L1) and any(str(j) == str(j)[::-1] for j in L1))

# para iterar todo lo que tienen un arreglo y corroborar que todos cumplen la condicion usamos un for como se puede ver
#  arriba  primero la condicion que queremos que se cumpla y luego el cilo for que recccore el arreglo el for es un apoyo
# a la funcion any y all para que esta funcion vea todo lo que contiene el arreglo y validar la condicion


"""
PARA ESTE EJERCICIO SE TIENE QUE VALIDAR UN ARREGLO CON 2 CONDICIONES
1.- QUE TODOS SEAN POSITIVOS
2.- QUE POR LO MENOS 1 SEA PALINDORMO NUMERICO

/////////////////
ENTRADA
/////////////////
5
12 9 61 5 14 

>> True

"""