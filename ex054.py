import datetime
contador = 0
for i in range (1, 8):
    ano = int(input('Digite o ano de nascimento da {} pessoa: '.format(i)))
    idade = datetime.date.today().year - ano
    if idade < 18:
        contador += 1

print('{} pessoas ainda não atingiram 18 anos.'.format(contador))