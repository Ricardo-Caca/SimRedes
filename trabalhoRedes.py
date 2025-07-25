import uuid, socket, random, struct, time

def get_mac_address():
    mac = uuid.getnode()
    mac_address = ':'.join(f'{(mac >> ele) & 0xff:02x}' for ele in range(40, -1, -8))
    return mac_address

# Endereços
macorigem = get_mac_address()
macdestino = "5c:cd:5b:2e:10:3d"
iporigem = socket.gethostbyname_ex(socket.gethostname())[-1][1]
ipdestino = "192.168.0.1"

# Portas
portaorigem = 80
portadestino = random.randint(1000, 8000)

seq_cliente = random.randint(0, 100000)
seq_servidor = random.randint(0, 100000)
   
def checksum():
   checksum = random.randint(0, 100)
   if(checksum == 10):
      return True
   return False


def encapsulamento():
    print("\n",AZUL+"-"*16, "------------|---- ENCAPSULAMENTO ----|------------","-"*17+RESET, sep='')  
def desencapsulamento(dadosbrutos):
    print("\n",VERMELHO+"-"*15, "|---------------- DESENCAPSULAMENTO ----------------|","-"*15+RESET, sep='') 
    print("\n", "="*32, " CONVERTENDO DADOS ", "="*32, sep='') 
    print("\n"," "*30," BINARIO PRA FLOAT\n")
    dadosTratados = []
    for i in dadosbrutos.flatten():
        dadosTratados.append(i)

    for i in dadosTratados:
        bits = struct.pack('!f', i)
        print(" "*20,''.join(f'{b:08b}' for b in bits),'→' , i)  
    print("\n","-"*82) 

def estabeleceConexao(): 
    print("\n",AMARELO+"-"*13, "|-----------|---- ESTABELECENDO CONEXÃO ----|-----------|","-"*13+RESET, sep='')  
    print("\n","="*36,   " ENDEREÇOS ","="*36, sep='')   
    print("Mac Origem",  " "*(71-len(macorigem)),f"{macorigem}")
    print("IP Origem",   " "*(72-len(iporigem)),f"{iporigem}")
    print("Mac Destino", " "*(70-len(macdestino)),f"{macdestino}")
    print("IP Destino",  " "*(71-len(ipdestino)), f"{ipdestino}")
    print("-"*83)

    time.sleep(0.4) # Dando delay pra leitura dos logs

    # 1 - Cliente envia SYN
    print("\n","="*17, " Cabeçalho TRANSPORTE - SYN (Cliente → Servidor) ","="*17, sep='')   
    print("Porta de Origem",     " "*(66 - len(str(portaorigem))),f"{portaorigem}")
    print("Porta de Destino",    " "*(65 - len(str(portadestino))),f"{portadestino}")
    print("Número de Sequência", " "*(62 - len(str(seq_cliente))),f"{seq_cliente}")
    print("Número de ACK",       " "*(68 - 1),0)
    print("Offset de Dados",     " "*(66 - len("20 bytes")),f"{5 * 4} bytes")
    print("Flags",               " "*(76 - len("{'URG': 0, 'ACK': 1, 'PSH': 0, 'RST': 0, 'SYN': 0, 'FIN': 0}")), 
        "{'URG': 0, 'ACK': 1, 'PSH': 0, 'RST': 0, 'SYN': 0, 'FIN': 0}")
    print("Tamanho da Janela",   " "*(64 - len(str(random.randint(1000, 65535)))), f"{random.randint(1000, 65535)}")
    print("Checksum"," "*(73 - len(hex(random.randint(0, 0xFFFF)))),   f"{hex(random.randint(0, 0xFFFF))}")

    print("Ponteiro Urgente",    " "*(65 - 1),f"{0}")

    print("-"*83)
    # Simulando INICIO da contagem do RTT. Tempo de ida + Tempo de volta
    tempo_inicio = time.time()
    time.sleep(random.uniform(0.09, 0.6))  # Simula delay de rede no envio
 

    # 2 - Servidor responde com SYN+ACK
    # Simulando FIM da contagem de RTT
    time.sleep(random.uniform(0.09, 0.2))  # Simula delay de rede no recebimento
    print("\n","="*13, " Cabeçalho TRANSPORTE - SYN+ACK 👍 (Servidor → Cliente) ","="*14, sep='')   
    print("Porta de Origem",     " "*(66 - len(str(portadestino))),f"{portadestino}")
    print("Porta de Destino",    " "*(65 - len(str(portaorigem))),f"{portaorigem}")
    print("Número de Sequência", " "*(62 - len(str(seq_cliente+1))),f"{seq_cliente+1}")
    print("Número de ACK",       " "*(68 - len(str(seq_servidor+1))),f"{seq_servidor+1}")
    print("Offset de Dados",     " "*(66 - len("20 bytes")),            f"{5 * 4} bytes")
    print("Flags",               " "*(76 - len("{'URG': 0, 'ACK': 1, 'PSH': 0, 'RST': 0, 'SYN': 0, 'FIN': 0}")), 
        "{'URG': 0, 'ACK': 1, 'PSH': 0, 'RST': 0, 'SYN': 0, 'FIN': 0}")
    print("Tamanho da Janela",   " "*(64 - len(str(random.randint(1000, 65535)))), f"{random.randint(1000, 65535)}")
    print("Checksum"," "*(73 - len(hex(random.randint(0, 0xFFFF)))),   f"{hex(random.randint(0, 0xFFFF))}")
    print("Ponteiro Urgente",    " "*(65 - 1),f"{0}")
    print("-"*83)

    
    # 3 - Cliente envia ACK final
    print("\n","="*15, " Cabeçalho TRANSPORTE - ACK 👍 (Cliente → Servidor) ","="*16, sep='')   
    print("Porta de Origem",     " "*(66 - len(str(portaorigem))),      f"{portaorigem}")
    print("Porta de Destino",    " "*(65 - len(str(portadestino))),     f"{portadestino}")
    print("Número de Sequência", " "*(62 - len(str(seq_cliente + 1))),  f"{seq_cliente + 1}")
    print("Número de ACK",       " "*(68 - len(str(seq_servidor + 1))), f"{seq_servidor + 1}")
    print("Offset de Dados",     " "*(66 - len("20 bytes")),            f"{5 * 4} bytes")
    print("Flags",               " "*(76 - len("{'URG': 0, 'ACK': 1, 'PSH': 0, 'RST': 0, 'SYN': 0, 'FIN': 0}")), 
        "{'URG': 0, 'ACK': 1, 'PSH': 0, 'RST': 0, 'SYN': 0, 'FIN': 0}")
    print("Tamanho da Janela",   " "*(64 - len(str(random.randint(1000, 65535)))), f"{random.randint(1000, 65535)}")
    print("Checksum"," "*(73 - len(hex(random.randint(0, 0xFFFF)))),   f"{hex(random.randint(0, 0xFFFF))}")

    print("Ponteiro Urgente",    " "*(65 - 1),f"{0}")
    print("-"*83)
    time.sleep(random.uniform(0.09, 0.6))  # Simula delay de rede no recebimento
    tempo_fim = time.time()

    time.sleep(0.4) # Dando delay pra leitura dos logs

    print("\n",VERDE + "-"*12, "|-----------|---- CONEXÃO ESTABELECIDA ✅ ----|-----------|","-"*12, sep='')  
    print(" "*41, f"RTT: {(tempo_fim - tempo_inicio)*1000:.2f}ms - Tempo de envio + resposta"+RESET, "\n")

def aplicação(dadosbrutos):
    print("\n","="*36, " APLICAÇÃO ","="*36, sep='')   

    print(f"DADOS BRUTOS:")
    for i in dadosbrutos:
       print(i.flatten()) 
    print("-"*83)
   
def transporte():
    tam_janela = random.randint(1000, 65535)
    checksum = hex(random.randint(0, 0xFFFF))

    print("\n","="*30, " Cabeçalho TRANSPORTE ","="*31, sep='')   
    print(f"Porta de Origem:      {portaorigem}")
    print(f"Porta de Destino:     {portadestino}")
    print(f"Número de Sequência:  {seq_cliente + 1 + 1}")
    print(f"Número de ACK:        {seq_servidor + 1}")
    print(f"Offset de Dados:      {5 * 4} bytes")
    print(f"Flags:                {{'URG': 0, 'ACK': 1, 'PSH': 1, 'RST': 0, 'SYN': 0, 'FIN': 0}}")
    print(f"Tamanho da Janela:    {tam_janela}")
    print(f"Checksum:             {checksum}")
    print(f"Ponteiro Urgente:     {0}")
    print(f"DADOS:                {0}")
    print("-"*83)

    segmento = {
        'porta_origem': portaorigem,
        'porta_destino': portadestino,
        'numero_sequencia': seq_cliente + 2,
        'numero_ack': seq_servidor + 1,
        'offset_dados': 5 * 4,
        'flags': {
            'URG': 0,
            'ACK': 1,
            'PSH': 1,
            'RST': 0,
            'SYN': 0,
            'FIN': 0
        },
        'tamanho_janela': tam_janela,
        'checksum': checksum,
        'ponteiro_urgente': 0
    }
    
    return segmento
def rem_transporte(dadosbrutos):
    print("\n","="*30, " Cabeçalho TRANSPORTE ","="*31, sep='')
    print("REMOVENDO cabeçalho de TRANSPORTE") 
    print("-"*83)
    aplicação(dadosbrutos)

def rede(segmento):
    tam_total = random.randint(40, 1500)  # Ex: tam_total = random.randint(40, 1500)
    identificacao = random.randint(0, 65535)
    checksum = hex(random.randint(0, 0xFFFF))
    tam_janela = random.randint(1000, 65535)
    
    print("\n","="*33, " Cabeçalho REDE ","="*34, sep='')    
    print(f"Porta de Origem:       {portaorigem}")
    print(f"Porta de Destino:      {portadestino}")
    print(f"Número de Sequência:   {seq_cliente + 1 + 1}")
    print(f"Número de ACK:         {seq_servidor + 1}")
    print(f"Offset de Dados:       {5 * 4} bytes")
    print(f"Flags:                 {{'URG': 0, 'ACK': 1, 'PSH': 1, 'RST': 0, 'SYN': 0, 'FIN': 0}}")
    print(f"Tamanho da Janela:     {tam_janela}")
    print(f"Checksum:              {checksum}")
    print(f"Ponteiro Urgente:      {0}")
    print(f"DADOS:                 {0}") 
    print(f"Versão:                {4}")
    print(f"IHL:                   {5} (20 bytes)")
    print(f"TOS:                   {0}")
    print(f"Tamanho Total:         {tam_total} bytes")
    print(f"Identificação:         {identificacao}")
    print(f"Flags:                 {"010"} (DF set)")
    print(f"Fragment Offset:       {0}")
    print(f"TTL:                   {64}")
    print(f"Protocolo:             {6} (TCP)")
    print(f"Checksum:              {checksum}")
    print(f"IP de Origem:          {iporigem}")
    print(f"IP de Destino:         {ipdestino}")
    print("-"*83)
    pacote = {
        'versao': 4,
        'ihl': 5,
        'tos': 0,
        'tamanho_total': tam_total, 
        'identificacao': identificacao,  # Ex: identificacao = random.randint(0, 65535)
        'flags': '010',  # DF set
        'fragment_offset': 0,
        'ttl': 64,
        'protocolo': 6,  # TCP
        'checksum': checksum,  # Ex: checksum = f"0x{random.randint(0, 0xFFFF):04x}"
        'ip_origem': iporigem,
        'ip_destino': ipdestino
    }
    pacote = segmento|pacote
    return pacote
def rem_rede():
    checksum = hex(random.randint(0, 0xFFFF))
    tam_janela = random.randint(1000, 65535)
    print("\n","="*33, " Cabeçalho REDE ","="*34, sep='')  
    print("REMOVENDO cabeçalho de REDE") 
    print(f"Porta de Origem:       {portaorigem}")
    print(f"Porta de Destino:      {portadestino}")
    print(f"Número de Sequência:   {seq_cliente + 1 + 1}")
    print(f"Número de ACK:         {seq_servidor + 1}")
    print(f"Offset de Dados:       {5 * 4} bytes")
    print(f"Flags:                 {{'URG': 0, 'ACK': 1, 'PSH': 1, 'RST': 0, 'SYN': 0, 'FIN': 0}}")
    print(f"Tamanho da Janela:     {tam_janela}")
    print(f"Checksum:              {checksum}")
    print(f"Ponteiro Urgente:      {0}")
    print(f"DADOS:                 {0}") 
    print("-"*83)

def enlace(pacote):
    tam_total = random.randint(40, 1500)  # Ex: tam_total = random.randint(40, 1500)
    identificacao = random.randint(0, 65535)
    checksum = hex(random.randint(0, 0xFFFF))
    tam_janela = random.randint(1000, 65535)
    
    print("\n","="*32, " Cabeçalho ENLACE ","="*33, sep='')  
    print(f"Porta de Origem:       {portaorigem}")
    print(f"Porta de Destino:      {portadestino}")
    print(f"Número de Sequência:   {seq_cliente + 1 + 1}")
    print(f"Número de ACK:         {seq_servidor + 1}")
    print(f"Offset de Dados:       {5 * 4} bytes")
    print(f"Flags:                 {{'URG': 0, 'ACK': 1, 'PSH': 1, 'RST': 0, 'SYN': 0, 'FIN': 0}}")
    print(f"Tamanho da Janela:     {tam_janela}")
    print(f"Checksum:              {checksum}")
    print(f"Ponteiro Urgente:      {0}")
    print(f"DADOS:                 {0}") 
    print(f"Versão:                {4}")
    print(f"IHL:                   {5} (20 bytes)")
    print(f"TOS:                   {0}")
    print(f"Tamanho Total:         {tam_total} bytes")
    print(f"Identificação:         {identificacao}")
    print(f"Flags:                 {"010"} (DF set)")
    print(f"Fragment Offset:       {0}")
    print(f"TTL:                   {64}")
    print(f"Protocolo:             {6} (TCP)")
    print(f"Checksum:              {checksum}")
    print(f"IP de Origem:          {iporigem}")
    print(f"IP de Destino:         {ipdestino}")  
    print(f"MAC de Destino:        {macdestino}")
    print(f"MAC de Origem:         {macorigem}")
    print(f"Tipo (EtherType):      0x0800  (IPv4)")
    print("-"*83)

    quadro = ','.join(f"'{k}':{v}" for k, v in pacote.items())
    quadro += f"'mac_destino':{macdestino},'mac_origem':{macorigem},'tipo':0x0800"
    return quadro

def rem_enlace(): 
    tam_total = random.randint(40, 1500)  # Ex: tam_total = random.randint(40, 1500)
    identificacao = random.randint(0, 65535)
    checksum = hex(random.randint(0, 0xFFFF))
    tam_janela = random.randint(1000, 65535)
    print("\n","="*32, " Cabeçalho ENLACE ","="*33, sep='')
    print("REMOVENDO cabeçalho de ENLACE") 
    print(f"Porta de Origem:       {portaorigem}")
    print(f"Porta de Destino:      {portadestino}")
    print(f"Número de Sequência:   {seq_cliente + 1 + 1}")
    print(f"Número de ACK:         {seq_servidor + 1}")
    print(f"Offset de Dados:       {5 * 4} bytes")
    print(f"Flags:                 {{'URG': 0, 'ACK': 1, 'PSH': 1, 'RST': 0, 'SYN': 0, 'FIN': 0}}")
    print(f"Tamanho da Janela:     {tam_janela}")
    print(f"Checksum:              {checksum}")
    print(f"Ponteiro Urgente:      {0}")
    print(f"DADOS:                 {0}") 
    print(f"Versão:                {4}")
    print(f"IHL:                   {5} (20 bytes)")
    print(f"TOS:                   {0}")
    print(f"Tamanho Total:         {tam_total} bytes")
    print(f"Identificação:         {identificacao}")
    print(f"Flags:                 {"010"} (DF set)")
    print(f"Fragment Offset:       {0}")
    print(f"TTL:                   {64}")
    print(f"Protocolo:             {6} (TCP)")
    print(f"Checksum:              {checksum}")
    print(f"IP de Origem:          {iporigem}")
    print(f"IP de Destino:         {ipdestino}") 
    print("-"*83)

def fisica(dadosbrutos, quadro):
    print("\n", "="*32, " Cabeçalho FÍSICA ", "="*33, sep='')   
    print("QUADRO:")
    for i in range(0, len(quadro), 83):
        print(quadro[i:i+83])
        
    print("\nDADOS:")
    for i in dadosbrutos:
       print(i.flatten())

    print("\n   CONVERTENDO PRA BINÁRIO")
    quadro_bytes = quadro.encode('utf-8')
    val_bin = ''.join(f'{byte:08b}' for byte in quadro_bytes)

    # Exibe quadro em binário (com quebra a cada 83 bits)
    print("\nQUADRO:")
    for i in range(0, len(val_bin), 83):
        print(val_bin[i:i+83])
    
    # Empacotando cada float e exibindo em bits
    dados_bin = ''
    for i in dadosbrutos.flatten():
        bits = struct.pack('!f', float(i))  # float32 big-endian
        bits_str = ''.join(f'{b:08b}' for b in bits)
        dados_bin += bits_str

    # Exibe dados em binário (com quebra a cada 83 bits)
    print("\nDADOS:")
    for i in range(0, len(dados_bin), 83):
        print(dados_bin[i:i+83])

    # Concatenando quadro + dados (em bytes)
    dados_bytes = b''.join(struct.pack('!f', float(i)) for i in dadosbrutos.flatten())
    quadro_completo_bytes = quadro_bytes + dados_bytes

    quadro_completo_bin = ''.join(f'{byte:08b}' for byte in quadro_completo_bytes)
    print("\nQUADRO + DADOS:")
    for i in range(0, len(quadro_completo_bin), 83):
        print(quadro_completo_bin[i:i+83])

    print("-"*83)

AZUL = "\033[34m"
AMARELO = "\033[33m"
VERMELHO = "\033[31m"
VERDE = "\033[32m"
MARROM = "\033[38;5;94m"
LARANJA = "\033[38;5;208m"
RESET = "\033[0m"
CIANO = "\033[36m"