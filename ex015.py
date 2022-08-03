#Escreva um programa que pergunte a quantidade de Km percorridos
#por um carro alugado e a quantidade de dias pelos quais ele foi usado
#Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia
#E R$0,15 por km rodado.

dias = int(input('Digite quantos dias o veiculo foi utilizado: '))
km = float(input('Digite quantos kms foram rodados: '))
valordia = float(dias * 60.00)
kmrodado = float(km * 0.15)
total = float(valordia + kmrodado)

print('O Veiculo usado {0} dias e foi rodado {1} Km. \nO valor pelos dias alugados é R${2}. \nO Valor equivalente aos Kms Rodados é R${3}. \nO total a Pagar é R${4}.'.format(dias, km, valordia, kmrodado, total))

