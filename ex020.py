#O mesmo professor do desafio anterior quer sortear a ordem de
# apresentacao de trabalho dos alunos. Faça um programa que leia o
# nome dos quatro alunos e mostre a ordem sorteada.

import random
n1 = input('Digite o Primeiro Nome: ')
n2 = input('Digite o Segundo Nome: ')
n3 = input('Digite o Terceiro Nome: ')
n4 = input('Digite o Quarto Nome: ')

lista = [n1, n2, n3, n4]
random.shuffle(lista)

print('A ordem da apresentação será : ')
print(lista)
