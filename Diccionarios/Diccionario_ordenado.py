#para este ejercicio se pudieron usar tanto los OrderedDict como los diccionarios ordinales ya que en versiones
#más recientes hacen lo mismo pero aqui se uso el OrderedDict

from collections import OrderedDict
n= int(input())
Dic1=OrderedDict()
for _ in range(n):

    h1 = list(map(str, input().rstrip().split())) #ingreso una lista
    text = " ".join(h1[0:-1])  #aqui separo el texto
    num = int(h1[-1])          #aqui separo el numero
    if text in Dic1:
        Dic1[text]+=num
    else:Dic1[text]=num


print('CANDY' in Dic1) # se pregunta por el nombre  si queremos saber si ya esta el valor una llave asi
print(Dic1)

keys= list(Dic1.keys()) # retorna una lista con las llaves
print(keys)
values= list(Dic1.values())#Retorna una lista con los valores
print(values)

tam=len(keys)

for i in range(tam):
    print(f'{keys[i]} {values[i]}')

"""
ENTRADA

9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30


"""