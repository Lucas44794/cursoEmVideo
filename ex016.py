#Crie um programa que leia um número Real qualquer pelo teclado
#e mostre na tela a sua potção inteira. EX: Digite um número: 6.127
# o número 6.127 tem a parte inteira 6.
import math

num = float(input('Digite um numero Real: '))
a = int(num)
b = math.trunc(num)

print('{} usando int.'.format(a))
print(" {} usando trunc.".format(b))
