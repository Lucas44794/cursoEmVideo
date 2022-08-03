# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos Dólares ela pode comprar
# Cotação do Dia: 5,41

carteira = float(input('Digite quanto você tem na carteira: '))
cotacao = 5.41
conversao = carteira / cotacao

print('Você tem {} Reais Na carteira e pode comprar {:.2f} Dolares. \n Cotação do dia: {}'.format(carteira, conversao,
                                                                                              cotacao))
