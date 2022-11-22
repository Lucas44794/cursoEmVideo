from random import randint
computador = randint(0, 10)
jogador = 99
contador = 0
while jogador != computador:
    jogador = int(input('Digite um número: '))
    contador += 1
    if computador != jogador:
        print('Tente novamente!!')

print('-=' * 20)
print('Parabéns, você ganhou!!!')
if contador > 0:
    print('Foram necessarios {} tentativas para acertar.'.format(contador))
