n=5
Fib = []
a=1
b=0

for k in range(n):
    c = a+b
    a = b
    b = c

    Fib.append(a)# aqui regresa la sucesion de fibonanci en lista

Res=map(lambda a:a**3,Fib)  # aplicamos el map para que la funcion labda se aplique a todos los elementos de la lista

print(list(Res))

"""
Para este ejercio solo de le pasa un numero y este devolvera la una lista de los numeros de fibonanci eleveados al 
cubo el numnero que se le pasa es el limite de numeros de fibonaci que tendra el arreglo  
"""