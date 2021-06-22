a = [1, 2, 3, 4, 5]
d = 201
for i in range(d):
    ax=a[0]
    a = a[1:]
    a.append(ax)

print(a)

#segunda forma mas chica
b = [1, 2, 3, 4, 5]

c=b[d:] + b[:d]



print(c)