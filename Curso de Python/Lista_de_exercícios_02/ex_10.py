a = int(input('Digite o primerio número: '))
b = int(input('Digite o segundo número: '))

if a < b:
    soma = 0
    for i in range (a, b + 1):
        soma += i
    print(f"A soma dos números inteiros de {a} até {b} é: {soma}")
else:
    print("O valor de 'a' deve ser menor que o valor de 'b'.")