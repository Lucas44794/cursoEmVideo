import datetime
nasct = int(input('Ano de nascimento: '))
idade = datetime.date.today().year - nasct

if idade > 19:
    print('Seu alistamento foi a {} anos'.format(idade - 18))
elif idade == 19:
    print('Seu alistamento foi a {} ano'.format(idade - 18))
elif idade == 18:
    print('Seu alistamento é neste ano, não preca o prazo, corra e faça já o seu!')
elif idade == 17:
    print('Seu alistamento será em {} ano'.format(18 - idade))
else:
    print('Seu alistamento será em {} anos'.format(18 - idade))