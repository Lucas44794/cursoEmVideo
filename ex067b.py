while True:
    print('=' * 30)
    print('Tabuada')
    print('=' * 30)
    print('Números negativos encerram o programa')
    num = int(input('Tabuada a ser exibida: '))
    tab = 0
    if num < 0:
        break
    else:
        for i in range(1, 11):
            print(f'{num} x {i} = {num * i}')
print('=' * 30)
print('FIM')