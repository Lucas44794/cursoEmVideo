import random

print('Seja bem vindo ao jogo')
print('Jokenpo - Pedra, Papel ou Tesoura!')
print('')
print('Suas Opções:')
print('[ 1 ] PEDRA')
print('[ 2 ] PAPEL')
print('[ 3 ] TESOURA')
opcao = int(input('Qual a sua Jogada: '))
lista = ["pedra", "papel", "tesoura"]
computador = random.randint(0,3)
print('O Computador Jogou {}!'.format(lista[computador]))
if computador == 0:
    if opcao == 1:
        print('Empate!')
    elif opcao == 2:
        print('Você Ganhou!!!')
    elif opcao == 3:
        print('Você Perdeu!')
elif computador == 1:
    if opcao == 1:
        print('Você Perdeu!')
    elif opcao == 2:
        print('Empate!')
    elif opcao == 3:
        print('Você Ganhou!')
elif computador == 2:
    if opcao == 1:
        print('Você Ganhou!')
    elif opcao == 2:
        print('Você Perdeu!')
    elif opcao == 3:
        print('Empate!')
