nome = str(input('Informe o seu nome: ')).capitalize()
tentativas = 3

while tentativas > 0:
    senha = str(input('Informe a sua senha: '))

    if senha == '123456':
        print(f'Olá, {nome}. Seja bem-vindo ao nosso banco!')
        break
    else:
        tentativas -=1
        if tentativas == 0:
            print("Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.")
        else:
            print(f'Senha incorreta! Você ainda tem {tentativas} tentativas.”')
        