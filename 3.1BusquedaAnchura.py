from collections import deque

def bfs(grafo, nodo_inicial, nodo_objetivo):
    visitados = set()
    cola = deque([[nodo_inicial]])

    while cola:
        camino = cola.popleft()
        nodo = camino[-1]

        if nodo in visitados:
            continue

        visitados.add(nodo)

        if nodo == nodo_objetivo:
            return camino

        for vecino in grafo.get(nodo, []):
            nuevo_camino = list(camino)
            nuevo_camino.append(vecino)
            cola.append(nuevo_camino)

    return None

# Ejemplo de uso
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

inicio = 'A'
objetivo = 'F'

camino = bfs(grafo, inicio, objetivo)

if camino:
    print("Camino encontrado:", camino)
else:
    print("No se encontró un camino.")
