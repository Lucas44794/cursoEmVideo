primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão de PA: '))
contador = 1
termo = primeiro
while contador <= 10:
    contador += 1
    print('{}'.format(termo), end='')
    termo += razao
    if contador <= 10:
        print(' -> ', end='')

print('\nFIM')