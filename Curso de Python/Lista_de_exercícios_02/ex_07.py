primeiro_termo = int(input('Informe o primeiro termo: '))
quantidade_termos = int(input('Informe a quantidade de termos: '))
razao = int(input('Informe a razão: '))

for i in range (quantidade_termos):
    termos = primeiro_termo + (i * razao)
    print("-->",termos, end=" ")