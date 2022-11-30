from random import randint
vitoria = 0
print('Impar ou Par?')
while True:
    computador = randint(1, 10)
    jogador = int(input('Digite seu Número: '))
    impPar = str(input('Impar ou Par? ')).strip().lower()[0]
    soma = computador + jogador
    if impPar == 'i' and soma % 2 == 1:
        print('Jogador Vendeu')
        vitoria += 1
        print(f'O computador jogou {computador}')
    elif impPar == 'i' and soma % 2 == 0:
        print('jogador PERDEU!')
        print(f'O computador jogou {computador}')
        break
    elif impPar == 'p' and soma % 2 == 0:
        print('Jogador VENCEU!')
        print(f'O computador jogou {computador}')
        vitoria += 1
    elif impPar == 'p' and soma % 2 == 1:
        print('Jogador PERDEU!')
        print(f'O computador jogou {computador}')
        break
    else:
        print('Entrada Incorreta')