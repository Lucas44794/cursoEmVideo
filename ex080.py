lista = list()
for contador in range(0,5):
    num = int(input('Digite um número: '))
    if contador == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado ao final da lista!!!')
    else:
        posicao = 0
        while posicao < len(lista):
            if num <= lista[posicao]:
                lista.insert(posicao, num)
                print(f'Adicionado na posição {posicao}')
                break
            posicao += 1
print('~' * 30)
print('Os valores digitados em ordem são: ')
print(lista)