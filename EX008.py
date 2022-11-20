metro = float(input('Digite o valor em metros: '))
decimetro = int(metro * 10);
centimetro = int(decimetro * 10);
milimetro = int(centimetro * 10);
decametro = metro / 10;
hectometro = decametro / 10;
quilometro = hectometro / 10;

print('A Conversão em KM é {} Quilômetros'.format(quilometro))
print('A Conversão em hm é {} Hectômetros'.format(hectometro))
print('A Conversão em dam é {} decâmetros'.format(decametro))
print('A distancia digitada foi {} metros'.format(metro))
print('A Conversão em dm é {} decímetros'.format(decimetro))
print('A Conversão em cm é {} centímetros'.format(centimetro))
print('A Conversão em mm é {} milímetros'.format(milimetro))