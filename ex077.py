palavra = ('aprender', 'programar', 'linguagem', 'python', 'curso',
           'gratis', 'estudar', 'praticar', 'trabalhar',
           'mercado', 'programador', 'futuro', )

for p in palavra:
    print('\nNa palavra {} temos '.format(p.upper()))
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')