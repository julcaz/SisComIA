import heapq

def a_estrella(grafo, heuristica, inicio, objetivo):
  
  
    cola_prioridad = []
    heapq.heappush(cola_prioridad, (heuristica[inicio], 0, [inicio]))
    visitados = set()

    print(f"Iniciando búsqueda A* desde '{inicio}' hacia '{objetivo}'\n")

    while cola_prioridad:
        f_actual, g_actual, camino = heapq.heappop(cola_prioridad)
        nodo_actual = camino[-1]

        print(f"Visitando nodo: {nodo_actual} | Costo acumulado: {g_actual} | f(n)={f_actual}")
        
        if nodo_actual in visitados:
            continue

        visitados.add(nodo_actual)

        if nodo_actual == objetivo:
            print("\n¡Nodo objetivo encontrado!")
            return camino, g_actual

        for vecino, costo in grafo.get(nodo_actual, []):
            if vecino not in visitados:
                g_nuevo = g_actual + costo
                f_nuevo = g_nuevo + heuristica.get(vecino, float('inf'))
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                heapq.heappush(cola_prioridad, (f_nuevo, g_nuevo, nuevo_camino))
                print(f"  Agregando vecino: {vecino} con f(n): {f_nuevo} | Camino: {nuevo_camino}")

        print("-" * 50)

    return None, float('inf')


grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 5), ('E', 2)],
    'C': [('F', 3)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}


heuristica = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 6,
    'E': 1,
    'F': 0
}


inicio = 'A'
objetivo = 'F'


camino_encontrado, costo_total = a_estrella(grafo, heuristica, inicio, objetivo)


print("\n" + "=" * 50)
if camino_encontrado:
    print(f"Camino óptimo encontrado: {camino_encontrado}")
    print(f"Costo total del camino: {costo_total}")
else:
    print("No se encontró un camino al objetivo.")
