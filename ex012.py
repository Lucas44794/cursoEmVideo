preco = float(input('Digite o Preço do produto: R$ '))
porcentagem = (preco / 100) * 5
precoAtual = preco - porcentagem

print('O produto que custava R${:.2f}, na promoção com desconto de 5% passa a custar R${:.2f}'.format(preco, precoAtual))