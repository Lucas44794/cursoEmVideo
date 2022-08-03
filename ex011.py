#Faça um progeama que leia a largura e a altura de uma parede em metros
#calcule a sua area e a quantidade de tinta necessaria para pinta-la
#sabendo que cada litro de tinta pinta uma área de 2m²


altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a Largura da parede: '))
metros = altura*largura
tinta = metros/2
print('Para pintar uma parede de {} metros² \nserá necessario {} litros de tinta para pinta-lá.'.format(metros, tinta))