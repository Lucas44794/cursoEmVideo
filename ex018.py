import math
angulo = float(input('Digite o ângulo que você deseja: '))
rad = math.radians(angulo)
print('O ângulo de {} tem o Seno de {:.2f}'.format(angulo, math.sin(rad)))
print('O ângulo de {} tem o Cosseno de {:.2f}'.format(angulo,math.cos(rad)))
print(('O ângulo de {} tem a Tangente de {:.2f}'.format(angulo, math.tan(rad))))