# s = 'aabbbccdeacaac'
s = 'google'
Sin_rpetr = set(s)  # quitamos las repeticiones
Sin_rpetr = list(Sin_rpetr)  # la pasamos a lista para su mejro uso

Sin_rpetr.sort()  # acomodando aseguramos que va a agarrar el menor en orden alfabetico por si algunos son oguales como en el caso de
# google  (l vale 1) y (e vale 1) pero por orden alfabetico agarramos la letra e
print(Sin_rpetr)

Frec = []
Fin3num = []
Fin3carc = []

for i in range(len(Sin_rpetr)):
    Frec.append(s.count(Sin_rpetr[i]))

print(Frec)
print()

for _ in range(3):
    Max = Frec.index(max(Frec))  # me da el indice del mayor

    Fin3carc.append(Sin_rpetr[Max])  # como son simetricas las agrego el caracter donde encontro la mayor repeticion.

    Fin3num.append(Frec[Max])  # como son simetricas las agrego el numero más grande o el de mayor repeticion.

    Sin_rpetr.pop(Max)

    Frec.pop(Max)
# --------------------------------------------------------
Orden = set(Fin3num)  # veo cuantos repetidos hay            |
#   |
Orden = list(Orden)  # pasamos a lista                       |
#   |
Frec = None  # reutilizamos estas variables (numeros)        |
Sin_rpetr = None  # (caracteres)                             |
# --------------------------------------------------------

print(Fin3num)  # antes de ser acomodadas correctamente
print(Fin3carc)

print()

if len(Orden) == 1:  # todos son repetidos por lo tanto ordenamos alfabeticamnte y imprimimos
    Fin3carc.sort()
    for i in range(3):
        print(f'{Fin3carc[i]} {Fin3num[i]}')

elif len(Orden) == 2:  # dos son repetidos (mucha talacha para poca cosa)

    if Fin3num[0] == Fin3num[1]:  # son los de la izquierda
        Frec = Fin3carc[2]
        Fin3carc.pop()
        Fin3carc.sort()
        Fin3carc.insert(2, Frec)
        for i in range(3):
            print(f'{Fin3carc[i]} {Fin3num[i]}')

    elif Fin3num[1] == Fin3num[2]:  # o son los de la derecha
        Frec = Fin3carc[0]
        Fin3carc.pop(0)
        Fin3carc.sort()
        Fin3carc.insert(0, Frec)
        for i in range(3):
            print(f'{Fin3carc[i]} {Fin3num[i]}')


elif len(Orden) == 3:  # ninguno repetido
    for i in range(3):
        print(f'{Fin3carc[i]} {Fin3num[i]}')
