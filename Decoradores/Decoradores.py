def funcion_a(funcion_b):
    def funcion_c(*args, **kwargs):
        print('Antes de la ejecución de la función a decorar')
        result = funcion_b(*args, **kwargs)
        print('Después de la ejecución de la función a decorar')

        return result

    return funcion_c

@funcion_a
def suma(a, b):
    return a + b

@funcion_a
def resta(a, b):
    return a - b

print(suma(77,0))

print(resta(10,3))

"""
Antes de la ejecución de la función a decorar
Después de la ejecución de la función a decorar
77
Antes de la ejecución de la función a decorar
Después de la ejecución de la función a decorar
7

"""