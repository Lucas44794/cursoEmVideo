#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
import math
nome = input('Digite o nome do funcionario: ')
salario = float(input('Digite o Salario do Funcionario: R$'))
novosalario = ((salario/100)*15)+salario

print('Olá {}, O seu Salario antigo era R${} e o novo salario será R${:.2f}.'.format(nome, salario, novosalario))