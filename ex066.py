cont = valor = 0
while True:
    num = int(input('Digite um valor [999 para terminar]: '))
    if num == 999:
        break
        cont = cont
    else:
        cont += num
        valor += 1
print('Foram digitados {} números e a soma deles é {}'.format(valor, cont))