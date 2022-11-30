print('--' * 30)
print('SEQUENCIA DE FIBONACCI')
print('--' * 30)
termos = int(input('Quantos termos você quer mostrar? '))
print('~~' * 30)
n1 = 0
n2 = 1
contador = 3
print('{} - {}'.format(n1, n2), end='')
while contador <= termos:
    n3 = n1 + n2
    print(' - {}'.format(n3), end='')
    n1 = n2
    n2 = n3
    contador += 1
print('\nFIM')