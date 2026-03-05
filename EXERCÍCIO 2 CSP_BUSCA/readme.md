📑 Agendamento de Monitores - IA (Busca BFS)

Este projeto implementa um sistema de resolução de conflitos para agendamento de monitores 
acadêmicos utilizando algoritmos de Inteligência Artificial. O objetivo é encontrar uma alocação
válida de monitores em salas e horários, respeitando uma série de restrições pré-definidas.
O problema é modelado como um CSP (Constraint Satisfaction Problem) e resolvido através de uma Busca em Largura (BFS).

🚀 O Problema
O sistema deve alocar:
3 Monitores: M1, M2, M3.
2 Salas: Lab1, Lab2.
2 Horários: 14h, 16h.

⚖️ Regras de Negócio (Restrições)
Unicidade: Cada monitor deve ser alocado em exatamente uma sala e um horário.
Conflito de Recurso: Não pode haver dois monitores na mesma sala no mesmo horário.
M1: O monitor M1 não pode atuar às 16h.
M3: O monitor M3 só pode atuar no Lab2.

🛠️ Tecnologias Utilizadas
Linguagem: Python 3.x
Módulos Nativos:
collections.deque: Para gerenciamento eficiente da fila de busca.
itertools.product: Para geração combinatória do domínio de estados.

🧠 Lógica de ImplementaçãoA solução foi dividida em três pilares fundamentais:
Representação de Estado: Utilização de dicionários Python para mapear variáveis (monitores) a 
valores (sala, horário).Função de Validação: Um "juiz" que verifica se o estado parcial ou total
infringe qualquer uma das regras de negócio.Busca em Largura (BFS): Exploração nível a nível do espaço de estados,
garantindo a descoberta da primeira solução válida.

📈 Análise TeóricaModelo: CSP (Problema de Satisfação de Restrições).
Crescimento do Espaço: Exponencial ($O(b^d)$). Com 3 monitores e 4 slots, o espaço bruto possui
$4^3 = 64$ combinações.Poda (Pruning): O algoritmo realiza poda preventiva ao validar os estados antes de inseri-los na fila,
descartando ramos inteiros da árvore de busca que violam as restrições.






































































































