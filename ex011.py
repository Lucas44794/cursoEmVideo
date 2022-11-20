largura = float(input('Largura da Parede: '))
altura = float(input('Altura da Parede: '))
dimensao = altura * largura
tinta = dimensao / 2
print('Sua parede tem dimensão de {} x {} e sua área é de {}m²'.format(largura, altura, dimensao))
print('Para pintar essa parede, você precisará de {}l de tinta'.format(tinta))