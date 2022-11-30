qtd = preco = mais1000 = menor = total = soma = 0
while True:
    nome = str(input('Nome do Produto: ')).strip().upper()
    preco = float(input('Preço: R$'))
    qtd += 1
    soma += preco
    if preco > 1000:
        mais1000 += 1
    if qtd == 1:
        menor = qtd
        nomeproduto = nome
    elif preco < menor:
        nomeproduto = nome
        menor = preco
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper() [0]
    if continuar == 'N':
        break
print(' O total do pedido foi R${:.2f}, o pedido contem {} itens. \n O mais barato foi {} que custa R${:.2f}. \n {} produtos custam mais de R$1000.00.'.format(soma, qtd, nomeproduto, menor, mais1000))