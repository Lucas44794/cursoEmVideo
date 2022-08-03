#Escreva um programa que leia um valor em metros e o exiba convertido em centrimetros e milimetros


metros = float(input('Digite quantos metros a converter: '))
centimetros = metros*100
milimetros = centimetros*10

print('Foi digitado {} Metros, que é igual a {} centimetros e é igual a {} milimetros'.format(metros, centimetros, milimetros))