import datetime
ano = int(input('Digite o ano que quer analizar? Digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Este é um ano Bissexto!')
else:
    print('Este não é um ano Bissexto!')