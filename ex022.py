nome = input('Digite seu nome completo: ')
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome contem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e tem {} letras.'.format(nome, nome.find(' ')))