times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',
         'Flamengo', 'Vasco', 'Chapecoence', 'Atlético', 'Botafogo',
         'Atlético-Pr', 'Bahia', 'São Paulo', 'Fluminense', 'Sport-Recife',
         'Ec Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-Go')

print(f'Os 4 primeiros colocados na tabela do brasileirão são: \n {times[0:5]}')
print('=-' * 40)
print(f'Os ultimos 4 colocados: \n {times[-4:]}')
print('=-' * 40)
print(f'Times em ordem Alphabeticas: \n {sorted(times)}')
print('=-' * 40)
print(f'O Chapecoence está na {times.index("Chapecoence")+1} posição')