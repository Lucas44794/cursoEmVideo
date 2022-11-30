valor = int(input('Valor: R$'))
contador = cinquenta = vinte = cinco = um = 0
while True:
    if valor >= 50:
        cinquenta += 1
        valor -= 50
    elif valor >= 20:
        vinte += 1
        valor -= 20
    elif valor >= 5:
        cinco += 1
        valor -= 5
    elif valor >= 1:
        um += 1
        valor -= 1
    else:
        break

if cinquenta > 0:
    print('Foram sacadas {} notas de Cinquenta Reais'.format(cinquenta))
if vinte > 0:
    print('Foram sacadas {} notas de Vinte Reais'.format(vinte))
if cinco > 0:
    print('Foram sacadas {} notas de Cinco Reais'.format(cinco))
if um > 0:
    print('Foram sacadas {} notas de Um Real'.format(um))

