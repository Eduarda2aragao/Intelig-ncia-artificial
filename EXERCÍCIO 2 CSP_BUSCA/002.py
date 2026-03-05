from collections import deque
from itertools import product

# ---------------------------------------------------------
# 1. Definição do Problema (Dados)
# ---------------------------------------------------------
monitores = ["M1", "M2", "M3"]
salas = ["Lab1", "Lab2"]
horarios = ["14h", "16h"]

# Criamos o domínio: todas as combinações possíveis de (sala, horário)
# Isso gera: [('Lab1', '14h'), ('Lab1', '16h'), ('Lab2', '14h'), ('Lab2', '16h')]
dominio = list(product(salas, horarios))

# ---------------------------------------------------------
# 2. Representação de Estado
# ---------------------------------------------------------
def estado_inicial():
    # O estado é um dicionário vazio: {}
    # À medida que avançamos, será: {"M1": ("Lab1", "14h"), ...}
    return {}

# ---------------------------------------------------------
# 3. Função Valido (Verificação de Conflitos e Regras)
# ---------------------------------------------------------
def valido(estado):
    alocados = []
    
    for monitor, (sala, horario) in estado.items():
        # Regra: Não pode haver dois monitores na mesma sala no mesmo horário
        if (sala, horario) in alocados:
            return False
        alocados.append((sala, horario))
        
        # Regra específica 3: O monitor M1 não pode atuar às 16h
        if monitor == "M1" and horario == "16h":
            return False
            
        # Regra específica 4: O monitor M3 só pode atuar no Lab2
        if monitor == "M3" and sala != "Lab2":
            return False
            
    return True

# ---------------------------------------------------------
# 4. Função Gerar Estados
# ---------------------------------------------------------
def gerar_estados(estado):
    novos_estados = []
    
    # Descobrimos qual o próximo monitor da lista que ainda não foi alocado
    # Se o estado tem len 0, pegamos monitores[0]. Se tem len 1, pegamos monitores[1].
    indice = len(estado)
    if indice < len(monitores):
        proximo_monitor = monitores[indice]
        
        # Tentamos colocar esse monitor em cada uma das opções do domínio
        for opcao in dominio:
            novo_estado = estado.copy()
            novo_estado[proximo_monitor] = opcao
            
            # Só adicionamos se a configuração parcial for válida
            if valido(novo_estado):
                novos_estados.append(novo_estado)
                
    return novos_estados

# ---------------------------------------------------------
# 5. Busca BFS (Breadth-First Search)
# ---------------------------------------------------------
def bfs():
    # Iniciamos a fila com o estado vazio
    fila = deque([estado_inicial()])
    
    while fila:
        # Retira o estado mais antigo (Largura)
        estado_atual = fila.popleft()
        
        # Se o estado atual já tem todos os monitores, encontramos a solução
        if len(estado_atual) == len(monitores):
            return estado_atual
        
        # Gera os próximos estados válidos e coloca na fila
        for proximo in gerar_estados(estado_atual):
            fila.append(proximo)
            
    return None

# ---------------------------------------------------------
# 6. Execução e Impressão da Solução
# ---------------------------------------------------------
solucao = bfs()

if solucao:
    print("--- Solução Encontrada ---")
    # Ordenamos para imprimir M1, M2, M3 em ordem
    for m in monitores:
        sala, hora = solucao[m]
        print(f"Monitor: {m} | Local: {sala} | Horário: {hora}")
else:
    print("Nenhuma solução satisfaz todas as restrições.")