#Escreva um programa que converta uma temperatura digitada em ºC e converta para  ºF

opcao = input('Digite a opção desejada \n Digite 1 para converter de ºC para ºF \n Digite 2 para converter de ºF para ºC \n Digite: ')

if opcao == "1" :
    temperatura = float(input('Digite a Temperatura em Graus Celsius: '))
    F = (temperatura*(9/5)+32)
    print('A conversão de {}ºC para ºF é: {}ºF.'.format(temperatura, F))
elif opcao =='2' :
    temperatura = float(input('Digite a Temperatura em Graus Fahrenheit: '))
    f = ((temperatura - 32) * (5/9))
    print('A conversão de {}ºF para ºC é: {}ºC.'.format(temperatura, f))
else :
    print('Opção Invalida.')
