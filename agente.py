import networkx as nx
import matplotlib.pyplot as plt
import random

# Crear un grafo completo aleatorio con distancias entre nodos
def crear_grafo_completo_aleatorio(n):
    G = nx.complete_graph(n)
    for u, v in G.edges():
        if u != v:
            G[u][v]['distancia'] = random.randint(1, 100)  # Distancias aleatorias
    return G

# Calcular la longitud de una ruta
def calcular_longitud_ruta(G, ruta):
    longitud = 0
    for i in range(len(ruta) - 1):
        longitud += G[ruta[i]][ruta[i + 1]]['distancia']
    return longitud

# Algoritmo del agente viajero con búsqueda aleatoria
def agente_viajero_busqueda_aleatoria(G, iteraciones):
    nodos = list(G.nodes())
    mejor_ruta = nodos[:]
    mejor_longitud = calcular_longitud_ruta(G, mejor_ruta)
    peor_ruta = nodos[:]
    peor_longitud = mejor_longitud

    rutas_probadas = []

    for _ in range(iteraciones):
        # Generar una ruta aleatoria
        ruta_actual = nodos[:]
        random.shuffle(ruta_actual)

        # Calcular la longitud de la ruta actual
        longitud_actual = calcular_longitud_ruta(G, ruta_actual)

        # Actualizar la mejor ruta si es necesario
        if longitud_actual < mejor_longitud:
            mejor_ruta = ruta_actual[:]
            mejor_longitud = longitud_actual

        # Actualizar la peor ruta si es necesario
        if longitud_actual > peor_longitud:
            peor_ruta = ruta_actual[:]
            peor_longitud = longitud_actual

        rutas_probadas.append((ruta_actual, longitud_actual))

    return mejor_ruta, mejor_longitud, peor_ruta, peor_longitud, rutas_probadas

# Crear un grafo aleatorio con 5 nodos (puedes cambiar el número de nodos)
nodos = 5
grafo = crear_grafo_completo_aleatorio(nodos)

# Resolver el problema del agente viajero
ruta_optima, longitud_optima, peor_ruta, longitud_peor, rutas_probadas = agente_viajero_busqueda_aleatoria(grafo, 10000)

# Visualizar el grafo y la ruta óptima
pos = nx.spring_layout(grafo)
nx.draw(grafo, pos, with_labels=True)
ruta_optima.append(ruta_optima[0])  # Agregar el nodo de inicio al final para cerrar el ciclo
nx.draw_networkx_nodes(grafo, pos, nodelist=ruta_optima, node_color='r')
nx.draw_networkx_edges(grafo, pos, edgelist=[(ruta_optima[i], ruta_optima[i + 1]) for i in range(len(ruta_optima) - 1)], edge_color='r', width=2)
plt.show()

print("Ruta óptima:", ruta_optima)
print("Longitud óptima:", longitud_optima)
print("Peor ruta:", peor_ruta)
print("Longitud peor ruta:", longitud_peor)
