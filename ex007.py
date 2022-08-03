#Desenvolva um programa que leia as duas notas de um aluno
#Calcule e mostre a sua média

nome = input('Digite o Nome do Aluno: ')
nota = float(input('Digite a Nota 1: '))
nota2 = float(input('Digite a Nota 2: '))

media = (nota+nota2)/2

print('A nota Do {} é {} e {}. \n Sua Média é {}'.format(nome, nota, nota2, media))
