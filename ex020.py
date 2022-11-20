import random

nome1 = input('Digite o Primeiro Nome: ')
nome2 = input('Digite o Segundo Nome: ')
nome3 = input('Digite o Terceiro Nome: ')
nome4 = input('Digite o Quarto Nome: ')
lista = [nome4, nome3, nome2, nome1]
random.shuffle(lista)

print('A ordem de apresentação será: ')
print(lista)