lado1 = float(input('Primeiro Segmento: '))
lado2 = float(input('Segundo Segmento: '))
lado3 = float(input('Terceiro Segmento: '))
print('')
print('==' * 25)

if lado1 < lado3 + lado2 and lado2 < lado1 + lado3 and lado3 < lado2 + lado1:
    print('Os segmentos acima podem formar um triângulo')
    if lado1 == lado3 and lado1 == lado2:
        print('Triângulo Equilátero')
    elif lado1 == lado2 or lado1 == lado3:
        print('Triângulo Isóceles')
    else:
        print('Triângulo Escaleno')
else:
    print('Os segmentos acima não podem formar um triângulo')

print("==" * 25)