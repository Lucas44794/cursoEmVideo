maior = 0
menor = 0
for i in range ( 1 , 6):
    peso = float(input('Digite o peso da {}º pessoa: '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print('O maior peso foi {}Kg'.format(maior))
print('O menor peso foi {}Kg'.format(menor))