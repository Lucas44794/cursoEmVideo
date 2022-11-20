n1 = int(input('Digite o Primeiro Número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('O primeiro número é maior!')
elif n2 > n1:
    print('O segundo número é maior!')
elif n1 == n2:
    print('Não existe valor maior, os dois são iguais')
else:
    print('Entrada invalida!!!')