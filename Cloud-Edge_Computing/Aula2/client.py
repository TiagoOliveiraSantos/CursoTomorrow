import socket

s = socket.socket()
s.connect(('localhost', 12345))
temperatura = 10.5
umidade = 45.5

mensagem = f"{temperatura}, {umidade}"
s.send(mensagem.encode())

print("Retorno do servidor", s.recv(1024).decode())

s.close()