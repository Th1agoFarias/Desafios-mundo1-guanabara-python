""" co = float(input('Entre com o valor do cateto oposto: '))
ca = float(input('Entre com o valor do cateto adjacente: '))

hipotenusa = (ca ** 2 + co ** 2) ** (1/2)

print('\n*******************\n')
print(f"O valor da hipotenusa é: {hipotenusa} ") """

from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hipotenusa = hypot(co, ca)

print(f'A hipotenusa vai medir: {hipotenusa}')