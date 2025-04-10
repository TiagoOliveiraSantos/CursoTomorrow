from math import sqrt

numero = int(input('Infome um número: '))

dobro = numero * 2
tripo = numero * 3
raiz = sqrt(numero)

print(f'''
O dobro de {numero} é {dobro}
O triplo de {numero} é {tripo}
A raiz quadrada de {numero} é {raiz:.1f}
''')
