#Temos: 3 monitores: M1, M2, M3 ;2 salas: Lab1, Lab2 ;2 horários: 14h, 16h 
#Regras 
#1. Cada monitor deve ser alocado em exatamente uma sala e um horário. 
#2. Não pode haver dois monitores na mesma sala no mesmo horário. 
#3. O monitor M1 não pode atuar às 16h. 
#4. O monitor M3 só pode atuar no Lab2. 

from collections import deque
from itertools import product

# 1. Dados
monitores = ["M1", "M2", "M3"]
salas = ["Lab1", "Lab2"]
horarios = ["14h", "16h"]

# 2. Definição do Estado Inicial
def estado_inicial():
    return {}

# 3. Validação de Restrições
def valido(estado):
    ocupacao = {}
    for monitor, (sala, horario) in estado.items():
        # Regra 2: Não pode haver dois monitores na mesma sala/horário
        if (sala, horario) in ocupacao:
            return False
        ocupacao[(sala, horario)] = monitor
        
        # Regra 3: M1 não pode atuar às 16h
        if monitor == "M1" and horario == "16h":
            return False
            
        # Regra 4: M3 só pode atuar no Lab2
        if monitor == "M3" and sala != "Lab2":
            return False
            
    return True

# 4. Geração de Novos Estados
def gerar_estados(estado):
    novos_estados = []
    
    # Identifica qual o próximo monitor a ser alocado
    # (O tamanho do dicionário 'estado' indica quantos já foram alocados)
    indice = len(estado)
    if indice >= len(monitores):
        return []
    
    monitor_atual = monitores[indice]
    
    # Tenta todas as combinações de sala e horário
    for sala, horario in product(salas, horarios):
        novo_estado = estado.copy()
        novo_estado[monitor_atual] = (sala, horario)
        
        # Verifica se essa tentativa respeita as regras
        if valido(novo_estado):
            novos_estados.append(novo_estado)
            
    return novos_estados

# 5. Busca BFS
def bfs():
    fila = deque([estado_inicial()])
    
    while fila:
        estado = fila.popleft()
        
        # Se todos os monitores foram alocados, temos uma solução
        if len(estado) == len(monitores):
            return estado
        
        for proximo in gerar_estados(estado):
            fila.append(proximo)
            
    return None

# 6. Execução
solucao = bfs()

if solucao:
    print("Solução encontrada:")
    for m, (s, h) in solucao.items():
        print(f"{m} -> {s} às {h}")
else:
    print("Nenhuma solução encontrada.")