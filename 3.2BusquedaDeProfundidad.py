def dfs(grafo, nodo_inicial, nodo_objetivo):
    pila = [[nodo_inicial]]  
    visitados = set()

    print(f"Iniciando DFS desde {nodo_inicial} buscando {nodo_objetivo}...\n")

    while pila:
        camino = pila.pop()  
        nodo = camino[-1]

        print(f"Analizando nodo: {nodo}")
        print(f"Camino actual: {camino}")

        if nodo in visitados:
            print(f"{nodo} ya fue visitado, se ignora.\n")
            continue

        visitados.add(nodo)

        if nodo == nodo_objetivo:
            print("\n¡Nodo objetivo encontrado!")
            return camino

        
        for vecino in reversed(grafo.get(nodo, [])):
            if vecino not in visitados:
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                pila.append(nuevo_camino)
                print(f"  -> Se agrega a la pila: {nuevo_camino}")

        print(f"Nodos visitados hasta ahora: {visitados}\n")

    return None


grafo = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['H'],
    'E': [],
    'F': ['I'],
    'G': [],
    'H': [],
    'I': []
}

inicio = 'A'
objetivo = 'I'

camino = dfs(grafo, inicio, objetivo)

if camino:
    print("\nCamino encontrado:", camino)
else:
    print("\nNo se encontró un camino.")
