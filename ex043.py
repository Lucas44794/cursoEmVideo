peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua Altura: '))

imc = peso / (altura * altura)
print('Seu imc é de {:.2f}'.format(imc))
if imc < 18.5:
    print('Magreza!')
elif imc > 18.4 and imc <= 24.9:
    print('Peso Normal')
    print('Menor Risco de Doenças Cardíacas e vasculares')
elif imc > 24.9 and imc <= 29.9:
    print('Sobrepeso')
    print('Fadiga, má circulação, varizes')
elif imc > 29.9 <= 34.9:
    print('Obesidade Grau I')
    print('Diabetes, angina, infarto, aterosclerose')
elif imc >= 35 < 40:
    print('Obesidade Grau II')
    print('Apneia do sono, falta de ar')
elif imc > 40:
    print('Obesidade Grau III')
    print('Refluxo, dificuldade para se mover, escaras, diabetes, infarto, AVC')
else:
    print('Tente Novamente!')
