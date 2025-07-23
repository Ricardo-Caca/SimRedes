import socket
import time

ip = '0.0.0.0'
porta = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((ip, porta))
sock.listen(1)  # aceita 1 conexão por vez
while True:
    print("Aguardando conexão TCP...")

    conn, endereco = sock.accept()
    print(f"Conectado por {endereco}")


    dados = conn.recv(1024)
    print("Recebido:", dados.decode())
    conn.sendall(dados)  # ecoa de volta
