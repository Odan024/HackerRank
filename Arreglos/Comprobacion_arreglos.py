#COmprobamos que por lo menos tenga un caracter de cada validacion en todo el arreglo


s="#$%@^&*kjnk svskjnbui h 4oi3hheuh /dfh uidshvhdsuihv suihc 0hrem89m4c02mw4xo;,wh fwhncoishmxlxfkjsahnxu83v 08 n8OHOIHIOMOICWHOFCMHEOFMCOEJMC0J09C 03J J3L;JMFC3JM3JC3'JIOO9MMJ099U N090N9 OOHOLNHNLLKNLKNKNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333000000000000000000000000000000000000000000000000000000000000000000000000000"

F1=False
F2=False
F3=False
F4=False
F5=False
c=0
for i in range(len(s)):
    if s[i].isalnum():
        F1=True

    if s[i].isalpha():
        F2=True

    if s[i].isdigit():
        F3=True

    if s[i].islower():
        F4=True

    if s[i].isupper():
        F5=True

    if F1==F2==F3==F4==F5 and i>(len(s)/2):break #Con esto decimos que por lo menos halla recorrido la mitad del arreglo

print(F1)
print(F2)
print(F3)
print(F4)
print(F5)