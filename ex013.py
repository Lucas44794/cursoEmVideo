salario = float(input('Digite o salario do funcionario: R$'))
atual = ((salario / 100) * 15) + salario
print('Um funcionario que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, atual))