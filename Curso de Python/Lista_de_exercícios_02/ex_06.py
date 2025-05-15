numero_01 = float(input('Digite o primeiro número positivo: '))
numero_02 = float(input('Digite o segundo número positivo: '))

print('''
[1] - Média ponderada, com pesos 2 e 3, respectivamente;
[2] - Quadrado da soma dos 2 números;
[3] - Cubo do menor número.
''')
opcao = int(input('Escolha uma opção: '))
       
if opcao == 1:
    media_peso_2 = 2
    media_peso_3 = 3
    media_ponderada = (numero_01 * media_peso_2 + numero_02 * media_peso_3) / (media_peso_2 + media_peso_3)
    print(f'A média ponderada entre os números {numero_01} e {numero_02}, com peso 2 e 3 respectivamente é {media_ponderada}')

elif opcao == 2:
    quadrado_soma = (numero_01 + numero_02) ** 2
    print(f'O quadrado da soma dos números {numero_01} e {numero_02} é {quadrado_soma}')

elif opcao == 3:
    if numero_01 < numero_02:
        cubo = numero_01 ** 3
        print(f'O cubo do número {numero_01} é {cubo}')
    else:
        cubo = numero_02 ** 3
        print(f'O cubo do número {numero_02} é {cubo}')

else:
    print(f'Opção incorreta!')