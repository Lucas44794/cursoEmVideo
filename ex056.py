contador = 0
maisVelho = 0
nomeMaisVelho = ''
mulheres = 0
contando = 0

for i in range(1, 5):
    print('-------- {}º PESSOA --------'.format(i))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ')
    contador += idade
    contando += 1
    if i == 1 and sexo in "Mm":
        maisVelho = idade
        nomeMaisVelho = nome
    else:
        if sexo in 'Mm' and maisVelho < idade:
            maisVelho = idade
            nomeMaisVelho = nome
    if sexo in 'Ff' and idade < 20:
        mulheres += 1
contador = contador / contando
print('--' * 30)
print('A média de idades do grupo é {} anos.'.format(contador))
print('O homem mais velho é {} e ele tem {} anos.'.format(nomeMaisVelho, maisVelho))
print('{} mulheres tem menos de 20 anos'.format(mulheres))