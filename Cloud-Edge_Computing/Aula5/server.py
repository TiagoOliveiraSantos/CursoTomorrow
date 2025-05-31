import socket
import json
import random
from cryptography.fernet import Fernet
from chave import chave

fernet = Fernet(chave)


s = socket.socket()
s.bind(('localhost', 12345))
s.listen(1)

print("Aguardando conexão...")

conn, addr = s.accept()
print(f"Conectado a {addr}")

mensagem_criptografada = conn.recv(1024)
mensagem = fernet.decrypt(mensagem_criptografada).decode()

# Convertendo JSON de volta para dicionário
dados = json.loads(mensagem)

print(f"Temperatura: {dados['temperatura']}°C, Umidade: {dados['umidade']}%")

ack = fernet.encrypt(b'Dados registrados com sucesso')
conn.send(ack)

conn.close()
