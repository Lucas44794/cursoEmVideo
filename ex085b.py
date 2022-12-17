num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    if valor % 2 == 1:
        num[1].append(valor)
num[1].sort()
num[0].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os números impares digitados foram: {num[1]}')