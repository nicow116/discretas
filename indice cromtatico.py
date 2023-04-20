import networkx as nx
import matplotlib.pyplot as plt

# Definimos el grafo de ejemplo
G = nx.Graph()
G.add_edges_from([(1,2),(1,3),(2,3),(2,4),(3,4),(4,5),(4,6),(5,6)])

# Calculamos el índice cromático del grafo
chrom_index = nx.chromatic_index(G)

# Asignamos diferentes colores a los nodos de cada conjunto en la partición del índice cromático
node_colors = {}
for i, color_set in enumerate(nx.coloring.greedy_color(G, strategy='largest_first').values()):
    for node in color_set:
        node_colors[node] = i

# Dibujamos el grafo con diferentes colores para cada conjunto
nx.draw(G, with_labels=True, node_color=[node_colors[node] for node in G.nodes()])

# Mostramos el grafo y el índice cromático en la consola
plt.show()
print("El índice cromático del grafo es:", chrom_index)
