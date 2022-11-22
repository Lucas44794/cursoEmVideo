from time import sleep
print('-=' * 20)
valTab = int(input('Digite A tabuada a ser exibida: '))
print('-=' * 20)
for a in range (1 , 11):
    print('{} x {} = {}'.format(valTab, a, valTab*a))
    sleep(0.3)
print('-=' * 20)
print('Finalizado!')
