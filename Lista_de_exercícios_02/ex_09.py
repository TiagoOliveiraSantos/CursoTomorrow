idade = 0
while True:
    idade = int(input('Digite a idade do aluno: '))
    if idade < 0:
        break
    print('Digite uma indade negativa para encerrar o programa')

print(f'Programa encerrado com sucesso!')