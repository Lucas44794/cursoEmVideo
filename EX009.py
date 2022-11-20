num = int(input('Digite um número para ver sua tabuada: '));
print('-' * 14);
tab = 11

for i in range(tab):
    valor = i * num
    print('{} x {} = {}'.format(num, i, valor))

print('-' * 14);