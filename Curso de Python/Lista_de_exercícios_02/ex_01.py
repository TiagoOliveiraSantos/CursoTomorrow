nota_01 = float(input('Informe a primeira nota: '))
nota_02 = float(input('Informe a segunda nota: '))
media = (nota_01 + nota_02) / 2

if media >= 6:
    print(f'Sua média foi {media:.2f}, Você foi APROVADO!')
else:
    print(f'Sua média foi {media:.2f}, Você foi REPROVADO!')