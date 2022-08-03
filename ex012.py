#Faça um algoritmo que leia  o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o preço do produto: '))
porcentagem = ((preco/100)*5)
precofinal = preco-porcentagem

print('O produto custa {} \nO Preço final com 5% de desconto é de {:.2f}.'.format(preco, precofinal))