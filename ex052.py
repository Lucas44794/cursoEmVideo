numero = int(input('Digite um Número: '))
print('-=' * 25)
total = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print('{} '.format(i), end=' ')
print('\n\033[mO número {} foi divisivel {} vezes'.format(numero, total))
if total == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
