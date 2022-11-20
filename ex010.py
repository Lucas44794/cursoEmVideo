valor = float(input('Digite o valor que você tem na carteira: '))
dolar = 5.12
atual = valor / dolar

print('Com R$ {} que você tem é possivel comprar US$ {:.2f} Dólares. '.format(valor, atual))
print('Cotação atual: 1 Dólar a R${}'.format(dolar))