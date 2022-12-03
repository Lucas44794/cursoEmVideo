from random import randint
num = (randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9))
print(f'Os 5 números gerados foram {num}')
print('O maior valor gerado foi {}'.format(max(num)))
print(f'O menor número gerado foi {min(num)}')