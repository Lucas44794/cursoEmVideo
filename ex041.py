from datetime import date
ano = int(input('Digite o ano de nascimento: '))
idade = date.today().year - ano
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 25:
    print('Sênior')
else:
    print('Master')