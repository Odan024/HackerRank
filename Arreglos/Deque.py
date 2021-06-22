from collections import deque


n = int(input())
d=deque()
for _ in range(n):
    o = list(map(str, input().rstrip().split()))
    if o[0]=='append':
        d.append(int(o[1]))

    elif o[0]=='appendleft':
        d.appendleft(int(o[1]))

    elif o[0]=='pop':
        d.pop()

    elif o[0]=='popleft':
        d.popleft()

deq=list(d)

for i in range(len(deq)):
    print(f'{deq[i]} ',end="")

"""
6
append 1
append 2
append 3
appendleft 4
pop
popleft
"""