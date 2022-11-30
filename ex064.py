soma = 0
cont = 0
num = 0
while num != 999:
    num = int(input('Digite um número [Digite 999 para parar]: '))
    cont += 1
    if num == 999:
        soma = soma
        cont -= 1
    else:
        soma += num
print('Você digitou {} números e a soma deles é {}'.format(cont, soma))