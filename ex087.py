par = list()
SegLinha = list()
total = terceiraColuna = segundaColuna = primeiraColuna = primeiraLinha = segundaLinha = terceiraLinha = 0
impares = list()
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o {l} {c} valor: '))
        total += matriz[l][c]
        if c == 2:
            terceiraColuna += matriz[l][c]
        elif c == 1:
            segundaColuna += matriz[l][c]
        elif c == 0:
            primeiraColuna += matriz[l][c]
        if l == 0:
            primeiraLinha += matriz[l][c]
        elif l == 1:
            segundaLinha += matriz[l][c]
            SegLinha.append(matriz[l][c])
        elif l == 2:
            terceiraLinha += matriz[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[l][c]} ]',end=' ')
    print()
print(f'A soma de todos os valores digitados foi {total}')
print(f'A soma dos valores digitados na terceira coluna são: {terceiraColuna}')
print(f'O maior valor digitado na segunda linha foi {max(SegLinha)}')