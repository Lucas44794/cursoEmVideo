num = []
for i in range(0, 7):
    num.append(float(input('Número: ')))
num.sort()
print('Os valores pares são: ', end=' ')
for a in num:
    if a % 2 == 0:
        print(a ,end=' ')
print()
print('Os valores impares digitados são: ',end=' ')
for a in num:
    if a % 2 == 1:
        print(a , end=' ')