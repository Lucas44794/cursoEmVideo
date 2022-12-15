lista = list()
contador = 0
while True:
    contador += 1
    lista.append(int(input('Digite um Valor: ')))
    resp = input('Quer continuar [S/N]: ').strip()[0]
    if resp in 'Nn':
        break
lista.sort(reverse=True)
print('-=' * 30)
print(f'Você digitou {contador} elementos')
print(f'Os valores em ordem decrescente são: {lista}')
if 5 in lista:
    print(f'O número 5 foi encotrado dentro da lista')
else:
    print('O número 5 não foi encontrado dentro da lista')