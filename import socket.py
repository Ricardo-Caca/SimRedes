import socket
import threading
import json
import numpy as np
from trabalhoRedes import aplicação 

# Recebe
def servidor_thread(ip_local, porta_local):
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((ip_local, porta_local))
    servidor.listen(1)
    print(f"[SERVIDOR] Aguardando conexão em {ip_local}:{porta_local}")
    conn, addr = servidor.accept()
    print(f"[SERVIDOR] Conectado por {addr}")

    while True:
        try:
            # conn.recv(1024) uma bib socket que significa receive
            dados = conn.recv(1024)
            if not dados:
                break
            print("[RECEBIDO]", json.loads(dados.decode()))

        except:
            break

    conn.close()
    servidor.close()

# Envia
def cliente_thread(ip_remoto, porta_remota):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((ip_remoto, porta_remota))
    print(f"[CLIENTE] Conectado a {ip_remoto}:{porta_remota}")

    while True:
        msg = input("Você: ")
        aplicação()
        if msg.lower() == "sair":
            break
        mensagem = np.array([[msg]], dtype=np.str_)
        dados = json.dumps(mensagem.tolist()).encode()

        cliente.sendall(dados)

    cliente.close()

# CONFIGURAÇÕES (troque conforme quem for A ou B)
meu_ip = '0.0.0.0'  # ou '127.0.0.1' se for teste local
porta_servidor = 5005       # minha porta para escutar
ip_destino = '192.168.0.11' # IP do outro peer
porta_destino = 5006        # porta do outro peer

# INICIA THREADS
threading.Thread(target=servidor_thread, args=(meu_ip, porta_servidor), daemon=True).start()
cliente_thread(ip_destino, porta_destino)
