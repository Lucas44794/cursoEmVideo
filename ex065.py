verificacao = 's'
cont = valor = soma = maior = menor = 0

while verificacao in 'sS':
    valor = int(input('Número: '))
    verificacao = str(input('Deseja continuar? [S/N]: ')).lower().strip()[0]
    soma += valor
    cont += 1
    if cont == 1:
        maior = valor
        menor = valor
    if valor > maior:
        maior = valor
    elif valor < menor:
        menor = valor
    else:
        maior = maior
        menor = menor
media = soma / cont
print('Foram digitados {} números e a média entre eles é {:.2f}'.format(cont, media))
print('O maior número digitado foi {}'.format(maior))
print('O menor número digitado foi {}'.format(menor))