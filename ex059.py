num1 = int(input('Primeiro Número: '))
num2 = int(input('Segundo Número: '))
opcao = 0
while opcao != 5:
    print('Menu de Opções')
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('Digite sua opção: '))
    print('-=' * 30)
    if opcao == 1:
        soma = num1 + num2
        print('{} + {} = {}'.format(num1, num2, soma))
        print('-=' * 30)
    elif opcao == 2:
        multiplica = num1 * num2
        print('{} x {} = {}'.format(num1, num2, multiplica))
        print('-=' * 30)
    elif opcao == 3:
        if num1 > num2:
            print('O maior é {}.'.format(num1))
            print('-=' * 30)
        elif num2 > num1:
            print('O maior é {}'.format(num2))
            print('-=' * 30)
        else:
            print('Ambos os números são iguais')
            print('-=' * 30)
    elif opcao == 4:
        print('Digite os novos números')
        num1 = int(input('Primeiro Número: '))
        num2 = int(input('Segundo Número: '))
        print('-=' * 30)
    else:
        if opcao == 5:
            print('Volte logo!!!')
        else:
            print('Opção Invalida, tente novamente!')
            print('-=' * 30)