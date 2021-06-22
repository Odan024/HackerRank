A,B = map(int,input().split(' '))

for i in range(1,A,2):
    print((".|."*i).center(B,"-"))
print("ODAN".center(B,"-"))

for i in range(A-2,-1,-2):
    print((".|." * i).center(B, "-"))