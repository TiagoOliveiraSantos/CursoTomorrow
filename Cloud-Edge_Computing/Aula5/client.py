import socket
import json
import random
from cryptography.fernet import Fernet
from chave import chave

fernet = Fernet(chave)


s = socket.socket()
s.connect(('localhost', 12345))

# Simulando a coleta de dados do sensor
dados = {
    "temperatura": round(random.uniform(20, 30), 2),
    "umidade": round(random.uniform(40, 60), 2)
}


mensagem = 'Dados sensíveis'

mensagem = json.dumps(dados).encode()  # Convertendo para JSON
mensagem_criptografada = fernet.encrypt(mensagem)
s.send(mensagem_criptografada)

print("Dados enviados criptografados:", mensagem_criptografada)

ack_criptografado = s.recv(1024)
ack = fernet.decrypt(ack_criptografado).decode()

print("Resposta do servidor:", ack)

s.close()