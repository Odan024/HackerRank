n = int(input())
Dic = {}

for i in range(n):
    text = input()
    if text in Dic:
        Dic[text] += 1

    else:
        Dic[text] = 1

# print(Dic)

print(len(Dic))
values = list(Dic.values())  # paso los valores a lista y los imprimo
for i in range(len(values)):
    print(f'{values[i]} ', end="")

"""
4
bcdef
abcdefg
bcde
bcdef
"""