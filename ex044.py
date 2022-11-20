print('=' * 30)
preco = float(input('Preço das Compras: R$'))
oldpreco = preco
print('=' * 30)
print('FORMAS DE PAGAMENTO')
print('=' * 30)
print('[ 1 ] à vista em dinheiro/cheque')
print('[ 2 ] à vista no cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
print('=' * 30)
opcao = int(input('Qual é a opção desejada: '))
if opcao == 1:
    preco = preco - ((preco / 100) * 10)
elif opcao == 2:
    preco = preco - ((preco / 100) * 5)
elif opcao == 3:
    preco = preco
elif opcao == 4:
    parcela = int(input('Digite quantas parcelas: '))
    print('=' * 30)
    preco = preco + ((preco / 100) * 20)
    print('Sua compra será parcelada em {}x e o valor de cada parcela será R${:.2f} com juros.'.format(parcela, preco / parcela))
else:
    print('Opção Invalida de pagamento!')

print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(oldpreco, preco))