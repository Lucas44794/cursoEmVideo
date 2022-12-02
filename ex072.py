numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
           'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
           'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    a = 0
    n = int(input('Número entre 0 e 20: '))
    if n >= 0 and n <= 20:
        print('{}'.format(numeros[n]))
        continuar = str(input('Deseja Continuar [S/N]: '))
        a = 1
        if continuar in 'nN':
            break
    if a == 0:
        print('Tente Novamente... ', end='')
    else:
        print('Bora de novo!!!')
print('Até logo!')