contIdade = homens = mulheres = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade > 18:
        contIdade += 1
    elif sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulheres += 1
    pergunta = str(input('Deseja Continuar? [S/N]: ')).strip().upper()[0]
    if pergunta == 'N':
        break

print(f'{contIdade} pessoas tem + de 18 anos')
print(f'{homens} Homens foram cadastrados.')
print(f'{mulheres} mulheres tem menos de 20 anos.')