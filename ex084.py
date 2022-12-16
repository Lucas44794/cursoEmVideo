temporario = list()
ativo = list()
maior = menor = 0

while True:
    temporario.append(str(input('Nome: ').lstrip()))
    temporario.append(float(input('Peso: ')))
    if menor == 0:
        menor = maior = temporario[1]
    ativo.append(temporario[:])
    if temporario[1] < menor:
        menor = temporario[1]
    if temporario[1] > maior:
        maior = temporario[1]
    temporario.clear()
    resposta = str(input('Deseja Continuar? [S/N]: '))
    if resposta in 'Nn':
        break
print(f'Foram digitados: {ativo}')
print(f'Foram cadastradas {len(ativo)} Pessoas.')
print(f'A(s) pessoa(s) mais pesada(s): ',end=' ')
for a in ativo:
    if a[1] == maior:
        print(a[0],end=' ')
print()
print(f'A(s) Pessoa(s) mais leve(s): ',end=' ')
for i in ativo:
    if i[1] == menor:
        print(i[0] ,end=' ')
