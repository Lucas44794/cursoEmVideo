velocidade = float(input('Digite a velocidade do carro: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você foi Multado por estar acima da velocidade máxima permitida de 80 km/h!!! \n A multa será de {:.2f}'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança')