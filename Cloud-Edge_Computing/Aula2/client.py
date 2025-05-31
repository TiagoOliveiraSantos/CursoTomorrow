import socket
import json
import random

s = socket.socket()
s.connect(('localhost', 12345))

# Simulando a coleta de dados do sensor
dados = {
    "temperatura": round(random.uniform(20, 30), 2),
    "umidade": round(random.uniform(40, 60), 2)
}

mensagem = json.dumps(dados)  # Convertendo para JSON
s.send(mensagem.encode())

print("Dados enviados:", mensagem)

print("Resposta do servidor:", s.recv(1024).decode())

s.close()