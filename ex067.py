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
        while tab < 10:
            tab += 1
            resultado = tab * num
            print(f'{num} x {tab} = {resultado}')
print('=' * 30)
print('FIM')