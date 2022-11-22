contador = 0
soma = 0
from time import sleep
for i in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(i)))
    if num % 2 == 0:
        soma += num
        contador += 1
    sleep(0.2)
print('=-' * 25)
print('A soma de {} numeros pares digitados é {}.'.format(contador, soma))