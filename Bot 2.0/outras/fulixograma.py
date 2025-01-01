import matplotlib.pyplot as plt  # Importa a biblioteca para criação de gráficos
import networkx as nx  # Importa a biblioteca para criação de grafos

# Criar o grafo direcionado
G = nx.DiGraph()

# Adicionar nós (arquivos)
G.add_node("1° Usuário", color='red')
G.add_node("2° index.html", color='blue')
G.add_node("3° style.css", color='green')
G.add_node("4° chat.js", color='purple')
G.add_node("5° app.py", color='orange')
G.add_node("6° response.py", color='pink')
G.add_node("7° database.py", color='brown')
G.add_node("8° faq.py", color='cyan')
G.add_node("9° ml_model.py", color='magenta')
G.add_node("10° perguntas.py", color='yellow')
G.add_node("11° train.py", color='lime')

# Adicionar arestas (relações entre os arquivos)
G.add_edges_from([
    ("1° Usuário", "2° index.html"),
    ("2° index.html", "3° style.css"),
    ("2° index.html", "4° chat.js"),
    ("4° chat.js", "5° app.py"),
    ("5° app.py", "6° response.py"),
    ("6° response.py", "7° database.py"),
    ("6° response.py", "8° faq.py"),
    ("8° faq.py", "6° response.py"),
    ("5° app.py", "9° ml_model.py"),
    ("9° ml_model.py", "6° response.py"),
    ("6° response.py", "7° database.py"),
    ("5° app.py", "10° perguntas.py"),
    ("5° app.py", "11° train.py"),
    ("11° train.py", "7° database.py")
])

# Criar a lista de cores das arestas de acordo com a cor dos nós
edge_colors = [G.nodes[u]['color'] for u, v in G.edges()]

# Desenhar o grafo com Circular Layout
plt.figure(figsize=(15, 15))  # Ajusta o tamanho da figura para uma melhor visualização
pos = nx.circular_layout(G)  # Usa o circular_layout para distribuir os nós em um círculo

# Desenha o grafo com setas, nós e arestas
nx.draw(G, pos, with_labels=True, node_size=8000, node_color=[G.nodes[n]['color'] for n in G.nodes()], 
        font_size=10, font_weight='bold', arrows=True, edge_color=edge_colors)

# Ajusta o título
plt.title("Fluxograma de Interação entre Arquivos (Circular Layout)", size=20)

# Exibe o gráfico
plt.show()
