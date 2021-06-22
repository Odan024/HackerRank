s = 'AABCAAADA'
sc=""
n=3
for i in range(len(s)):
    if(s[i] in sc)==False:
        sc=sc+s[i]
    if (i + 1) % n == 0:
        print(sc)
        sc=""
