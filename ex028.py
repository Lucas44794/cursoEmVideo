from random import randint
import time
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar')
print('-=-' * 20)
print('Pensando....')
print('-=-' * 20)
time.sleep(3)
jogador = int(input('Em que número eu pensei? '))
if jogador == computador:
    print('PARABÉNS!!! Você conseguiu vencer!')
else:
    print('Ganhei!!!!! Eu pensei no número {} e não no {}'.format(computador, jogador))