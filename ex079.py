num = list()
while True:
    n = int(input('Digite um número: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado. Não vou adicionar!')
    e = str(input('Quer continuar [S/N]: '))[0]
    if e in 'Nn':
        break
num.sort()
print(num)