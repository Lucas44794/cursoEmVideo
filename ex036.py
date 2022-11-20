valor = float(input('Valor da casa: R$'))
salario = float(input('Valor do salario: R$'))
anos = int(input('Quantos anos de financiamento: '))

anosAtual = anos * 12
valorCasa = valor / anosAtual

if valorCasa >= ((salario / 100) * 30):
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.'.format(valor, anos, valorCasa))
    print('Emprestimo NEGADO!')
else:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.'.format(valor, anos, valorCasa))
    print('Emprestimo APROVADO!')