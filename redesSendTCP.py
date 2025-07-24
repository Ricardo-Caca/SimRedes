import socket
import json
import numpy as np

ip_servidor = '192.168.0.11'
porta = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((ip_servidor, porta))
print(f"Conectado ao servidor em {ip_servidor}:{porta}")

# mensagem = {"nome": "Ricardo", "mensagem": "Ola servidor via TCP!"}

mensagem = np.array([[-0.52, 0.63, 0.0],[0.30000000000000004, 0.030000000000000027, 0.0]], dtype=np.float32)
dados = json.dumps(mensagem.tolist()).encode()

sock.sendall(dados)
print("Mensagem enviada.")

resposta = sock.recv(1024)
if resposta:
    print("Resposta recebida:", json.loads(resposta.decode()))
else:
    print("Sem resposta do servidor.")

sock.close()