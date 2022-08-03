#Um professor quer sortear um dos seus quatro alunos
# para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome do escolhido.

import random
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do Terceiro Aluno: ')
aluno4 = input('Digite o nome do Quarto Aluno: ')

lista = [aluno4, aluno3, aluno2, aluno1]

escolhido = random.choice(lista)

print('O escolhido foi: {}'.format(escolhido))

