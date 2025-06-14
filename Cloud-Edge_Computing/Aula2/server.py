import socket
import json

s = socket.socket()
s.bind(('localhost', 12345))
s.listen(1)

print("Aguardando conexão...")

conn, addr = s.accept()

print(f"Conectado a {addr}")
dados_recebidos = conn.recv(1024).decode()

# Convertendo JSON de volta para dicionário
dados = json.loads(dados_recebidos)

print(f"Temperatura: {dados['temperatura']}°C, Umidade: {dados['umidade']}%")

conn.send(b'Dados registrados com sucesso')

conn.close()
