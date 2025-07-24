import uuid
import socket
import os
import random
import struct 

def get_mac_address():
    mac = uuid.getnode()
    mac_address = ':'.join(f'{(mac >> ele) & 0xff:02x}' for ele in range(40, -1, -8))
    return mac_address


macorigem = get_mac_address()
macdestino = "5c:cd:5b:2e:10:3d"
iporigem = socket.gethostbyname_ex(socket.gethostname())[-1][1]
ipdestino = "192.168.0.1"

portaorigem = 80
portadestino = random.randint(1000, 8000)

seq_cliente = random.randint(0, 100000)
seq_servidor = random.randint(0, 100000)
   
dadosbrutos = [0.002, 0.03]

def checksum():
   checksum = random.randint(0, 100)
   if(checksum == 10):
      return True
   return False

def estabeleceConexao():
   print("=========|-----------|---- ESTABELECENDO CONEXÃO ----|-----------|=========")
   print("Mac Origem", macorigem)
   print("IP Origem", iporigem)
   print("Mac Destino", macdestino)
   print("IP Destino", ipdestino)
   print("========= Cabeçalho TRANSPORTE - SYN (Cliente → Servidor) =========")
   print(f"Porta de Origem:       {portaorigem}")
   print(f"Porta de Destino:      {portadestino}")
   print(f"Número de Sequência:   {seq_cliente}")
   print(f"Número de ACK:         {0}")
   print(f"Offset de Dados:       {5 * 4} bytes")
   print(f"Flags:                 {{'URG': 0, 'ACK': 0, 'PSH': 0, 'RST': 0, 'SYN': 1, 'FIN': 0}}")
   print(f"Tamanho da Janela:     {random.randint(1000, 65535)}")
   print(f"Checksum:              {hex(random.randint(0, 0xFFFF))}")
   print(f"Ponteiro Urgente:      {0}")
   print("==============================================================\n")

   print("========= Cabeçalho TRANSPORTE - SYN+ACK (Servidor → Cliente) =========")
   print(f"Porta de Origem:       {portadestino}")
   print(f"Porta de Destino:      {portaorigem}")
   print(f"Número de Sequência:   {seq_servidor}")
   print(f"Número de ACK:         {seq_cliente + 1}")
   print(f"Offset de Dados:       {5 * 4} bytes")
   print(f"Flags:                 {{'URG': 0, 'ACK': 1, 'PSH': 0, 'RST': 0, 'SYN': 1, 'FIN': 0}}")
   print(f"Tamanho da Janela:     {random.randint(1000, 65535)}")
   print(f"Checksum:              {hex(random.randint(0, 0xFFFF))}")
   print(f"Ponteiro Urgente:      {0}")
   print("===============================================================\n")

   print("========= Cabeçalho TRANSPORTE - ACK (Cliente → Servidor) =========")
   print(f"Porta de Origem:       {portaorigem}")
   print(f"Porta de Destino:      {portadestino}")
   print(f"Número de Sequência:   {seq_cliente + 1}")
   print(f"Número de ACK:         {seq_servidor + 1}")
   print(f"Offset de Dados:       {5 * 4} bytes")
   print(f"Flags:                 {{'URG': 0, 'ACK': 1, 'PSH': 0, 'RST': 0, 'SYN': 0, 'FIN': 0}}")
   print(f"Tamanho da Janela:     {random.randint(1000, 65535)}")
   print(f"Checksum:              {hex(random.randint(0, 0xFFFF))}")
   print(f"Ponteiro Urgente:      {0}")
   print("=============================================================\n")
   
   print("=========|-----------|---- CONEXÃO ESTABELECIDA ----|-----------|=========")
   

def aplicação(dadosbrutos):
    print("|-----------|---- APLICAÇÃO ----|-----------|")
    print(f"DADOS BRUTOS:{dadosbrutos}") 
    print("|-----------|-------------------|-----------|")
   
def transporte():
   print("========= Cabeçalho TRANSPORTE =========")
   print(f"Porta de Origem:       {portaorigem}")
   print(f"Porta de Destino:      {portadestino}")
   print(f"Número de Sequência:   {seq_cliente + 1 + 1}")
   print(f"Número de ACK:         {seq_servidor + 1}")
   print(f"Offset de Dados:       {5 * 4} bytes")
   print(f"Flags:                 {{'URG': 0, 'ACK': 1, 'PSH': 1, 'RST': 0, 'SYN': 0, 'FIN': 0}}")
   print(f"Tamanho da Janela:     {random.randint(1000, 65535)}")
   print(f"Checksum:              {hex(random.randint(0, 0xFFFF))}")
   print(f"Ponteiro Urgente:      {0}")
   print("===============================================================\n")
   

def rede():
   print("=========== Cabeçalho IPv4 ===========")
   print(f"Versão:                  {4}")
   print(f"IHL:                     {5} (20 bytes)")
   print(f"TOS:                     {0}")
   print(f"Tamanho Total:           {random.randint(40, 1500)} bytes")
   print(f"Identificação:           {random.randint(0, 65535)}")
   print(f"Flags:                   {"010"} (DF set)")
   print(f"Fragment Offset:         {0}")
   print(f"TTL:                     {64}")
   print(f"Protocolo:               {6} (TCP)")
   print(f"Checksum:                0x{random.randint(0, 0xFFFF):04x}")
   print(f"Endereço IP de Origem:   {iporigem}")
   print(f"Endereço IP de Destino:  {ipdestino}")
   print("================================================")
   

def enlace():
   print("=========== Cabeçalho ENLACE ===========")
   print(f"MAC de Destino:     {macdestino}")
   print(f"MAC de Origem:      {macorigem}")
   print(f"Tipo (EtherType):   0x0800  (IPv4)")
   print("==========================================")
   

def fisica(dadosbrutos):
    print("=========== CAMADA FÍSICA ===========")
    print("CONVERTENDO PRA BINÁRIO")
    dadosTratados = []
    for i in dadosbrutos.flatten():
        dadosTratados.append(i)
    for i in dadosTratados:
        bits = struct.pack('!f', i)
        print(i, '→' ,''.join(f'{b:08b}' for b in bits))
    print("|-----------|-------------------|-----------|")
