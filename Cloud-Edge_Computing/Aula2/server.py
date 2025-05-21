import socket

s = socket.socket()
s.bind(('localhost', 12345))
s.listen(1)

print("Aguardando conexão...")

conn, addr = s.accept()

print(f"Conectado a {addr}")
dados_recebidos = conn.recv(1024).decode()

temperadura, umidade = dados_recebidos.split(",")
print(f'Temperatura: {temperadura}ºC, Umidade: {umidade}')

conn.send(b'Dados recebidos com sucesso!')
conn.close()