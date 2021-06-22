def wrapper(f):
    def fun(l):
        # complete the function

        for i in range(len(l)):
            if len(l[i]) ==10:
                l[i]='91'+l[i]
            if l[i][0] == '0':
                l[i]='91'+l[i][1:]
            if l[i][0] == '+':
                l[i] = l[i][1:]

            a ='+'+l[i][0:2]
            b = l[i][2:7]
            c = l[i][7:12]
            l[i] = a+' '+b+' '+c
        f(l)

    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)



"""
ENTRADA

3
07895462130
919875641230
9195969878


SALIDA

+91 78954 62130
+91 91959 69878
+91 98756 41230


"""