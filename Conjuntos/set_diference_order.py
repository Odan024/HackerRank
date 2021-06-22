
input()

M = set(map(int, input().split()))

input()

N = set(map(int, input().split()))

R= M.symmetric_difference(N)

R = list(R)
R.sort()
for i in R:
    print(i)

"""
4           
2 4 5 9     
4           
2 4 11 12 
"""