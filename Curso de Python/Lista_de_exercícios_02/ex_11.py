e = int(input("Informe o espaço: "))
t = int(input("Informe o tempo: "))

if 1 <= e <= 500 and 1 <= t <= 100:
    v = e // t
    print(f"Velocidade alcançada: {v}")
else:
    print("Erro: Os valores devem estar no intervalo 1 <= e <= 500 e 1 <= t <= 100.")