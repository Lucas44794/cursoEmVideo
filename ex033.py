num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo Valor: '))
num3 = int(input('Terceiro Valor: '))
if num1 < num2 and num1 < num3:
    menor = num1
elif num2 < num1 and num2 < num3:
    menor = num2
else:
    menor = num3

if num1 > num2 and num1 > num3:
    maior = num1
elif num2 > num1 and num2 > num3:
    maior = num2
else:
    maior = num3

print('o menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))