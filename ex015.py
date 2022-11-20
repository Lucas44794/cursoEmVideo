dias = int(input('Digite quantos dias o carro permaneceu alugado: '))
km = float(input('Digite quantos quilometros foram rodados: '))
totalDias = dias * 60
totalKm = km * 0.15
total = totalDias + totalKm
print('O total gasto com a Diaria do veiculo foi R${:.2f} referentes a {} dias alugados'.format(totalDias, dias))
print('O total gasto com a rodagem foi R${:.2f}, referente aos {}Km percorridos'.format(totalKm, km))
print('O total a pagar é R${:.2f}'.format(total))