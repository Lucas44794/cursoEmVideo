numero = list()
impar = list()
par = list()

while True:
    numero.append(int(input('Digite um número: ')))
    while True:
        continuar = str(input('Deseja Continuar? [S/N]: '))[0]
        if continuar in 'SsNn':
            break
        else:
            print('Valor incorreto inserido, tente novamente!!!')
    if continuar in 'Nn':
        break
for v, i in enumerate(numero):
    if i % 2 == 0 and i != 0:
        par.append(i)
    elif i % 2 == 1:
        impar.append(i)
print(f'Os números digitados foram: {numero}')
print(f'Os números pares são: {par}')
print(f'Os números impares são: {impar}')
