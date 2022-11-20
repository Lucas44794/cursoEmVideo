nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota = (nota2 + nota1) / 2
if nota < 5:
    print('A média ficou {} e o aluno foi REPROVADO!'.format(nota))
elif nota  >= 5 and nota < 7:
    print('A média ficou {} e o aluno está de RECUPERAÇÃO!'.format(nota))
else:
    print('APROVADO com média {}. Meus parabéns!'.format(nota))