import networkx as nx
import matplotlib.pyplot as plt

# Creamos un grafo aleatorio con 8 nodos y 12 aristas
G = nx.gnm_random_graph(6, 6)

# Creamos una lista de colores para colorear las aristas
colors = ['r', 'g', 'b', 'c', 'm', 'y']

# Creamos una lista para llevar el seguimiento de los colores utilizados
used_colors = []

# Recorremos todas las aristas del grafo
for u, v in G.edges():

    # Obtenemos los colores asignados a las aristas adyacentes a u y v
    adjacent_colors_u = [G[u][adj]['color'] for adj in G.neighbors(u) if 'color' in G[u][adj]]
    adjacent_colors_v = [G[v][adj]['color'] for adj in G.neighbors(v) if 'color' in G[v][adj]]

    # Creamos un conjunto de colores adyacentes a las aristas de u y v
    adjacent_colors = set(adjacent_colors_u + adjacent_colors_v)

    # Buscamos el primer color de los utilizados que no está en el conjunto de colores adyacentes
    for color in used_colors:
        if color not in adjacent_colors:
            break
    else:
        # Si no encontramos ningún color utilizado que no esté en el conjunto de colores adyacentes, tomamos uno de la lista de colores
        color = colors[len(used_colors) % len(colors)]
        used_colors.append(color)

    # Asignamos el color encontrado a la arista (u, v)
    G[u][v]['color'] = color

# Dibujamos el grafo con las aristas coloreadas
nx.draw(G, with_labels=True, edge_color=[d['color'] for u, v, d in G.edges(data=True)])
print("Indice cromatico:"+str(len(used_colors)))
plt.show()
