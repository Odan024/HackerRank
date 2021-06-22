import cmath

z = complex('(1+2j)') # se peude introducir en formato de cadena simpre que sea un complejo con parte real y parte
                    # imaginaria. Otra forma seria complex(1,2) que seria equivalente a el complejo que esta en cadena
                    #en la line3. Tambien puede ir entre parentesis o sin ellos

print(abs(z))
print(cmath.phase(z))
