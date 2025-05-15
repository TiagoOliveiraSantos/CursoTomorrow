notas = 0
for i in range(1,11):
    nota = float(input(f'Digite a {i}ª nota: '))
    notas += nota
    i += 1
media = notas / (i - 1)
print(f'A sua média é {media:.2f}')