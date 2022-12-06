#FAÇA UM PROGHAMA QUE LEIA 5 VALORES NUMERICOS E GUARDE OS EM UMA LISTA.
# NO FINAL MOSTRE QUAL FOI O MAIOR E O MENOR VALOR DIGITADO E AS SUAS RESPECTIVAS POSIÇÕES NA LISTA.
num = list()
maior = list()
menor = list()
for i in range(0, 5):
    num.append(int(input(f'Digite o {i}º número: ')))
    if i == 0:
        maior = menor = num[i]
    else:
        if num[i] > maior:
            maior = num[i]
        if num[i] < menor:
            menor = num[i]
print('=-' * 30)
print(f'Os números digitados foram: {num}')
print(f'O maior número digitado foi {max(num)} e suas  posições foram: ', end=' ')
for a, v in enumerate(num):
    if v == maior:
        print(f'{a}...',end=' ')
print()
print(f'O menor número digitado foi {min(num)} e suas posições foram: ',end=' ')
for a, v in enumerate(num):
    if v == menor:
        print(f'{a}...',end=' ')
print()
