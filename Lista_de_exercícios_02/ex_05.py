numero = int(input('Digite um número: '))

if numero % 2 == 0:
    quadrado = numero ** 2
    print(f'O número {numero} é PAR e o seu QUADRADO é {quadrado}')
else:
    cubo = numero ** 3
    print(f'O número {numero} é ÍMPAR e o seu CUBO é {cubo}')