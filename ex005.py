#Faça um programa que leia um número inteiro e mostre o seu sucessor e antecessor.

n = int(input('Digite um numero: '))

print('O Numero Digitado foi {:^10}, Seu antecessor é {} e seu sucessor é {}.'.format(n, n-1, n+1))