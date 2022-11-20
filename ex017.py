import math
catoposto = float(input('Comprimento do cateto oposto: '))
catadj = float(input('Comprimento do cateto adjacente: '))
print('A Hipotenusa vai medir {:.2f}'.format(math.hypot(catoposto, catadj)))