soma = 0
contador = 0
for i in range (1 , 501 , 2):
    if i % 3 == 0:
        contador += 1
        soma = soma + i
print('A soma de todos os {} valores é {}.'.format( contador, soma))
