# script que

import math

a = float(input ("indica o valor correspondente ao cateto 'a': "))
b = float(input ("indica o valor correspondente ao cateto 'b': "))

hip = round(math.sqrt(a**2 + b**2),2)

print("O valor da hipotenusa é: \t", hip)
