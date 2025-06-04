from cryptography.fernet import Fernet

chave = Fernet.generate_key()
fernet = Fernet(chave)

mensagem = "Edge Computing".encode()

mensagem_segura = fernet.encrypt(mensagem)

print(f'Chave: {chave.decode()}')
print(f'Mensagem Criptorgrafada: {mensagem_segura.decode()}')