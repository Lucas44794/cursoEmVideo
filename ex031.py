distancia = float(input('Qual a distancia da sua viagem? '))
print('Você está prestes a fazer uma viagem de {}Km'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print('O preço da sua viagem é R${:.2f}'.format(preco))