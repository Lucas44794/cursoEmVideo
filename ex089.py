geral = list()
aluno = list()
while True:
    nome = str(input('Nome: ')).lstrip().capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota2 + nota1) / 2
    aluno.append([nome, [nota1, nota2], media])
    geral.append(aluno[:])
    aluno.clear()
    resp = input('Deseja continuar? [S/N]: ').strip()[0]
    while resp not in 'SsNn':
        print('Tente novamente....')
        resp = str(input('Deseja continuar? [S/N]: '))
    if resp in 'Nn':
        break
print(geral)
for i, a in enumerate(geral):
    print(f'{i:<4}{a[0][0]:<10}{a[0][2]:>8.1f}')