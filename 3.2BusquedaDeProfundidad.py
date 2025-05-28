from utils_8puzzle import *

def depth_first_search(start):
    visited = set()
    stack = [start]
    came_from = {tuple(start): None}

    while stack:
        current = stack.pop()
        if current == GOAL_STATE:
            print("\n¡Solución encontrada con Búsqueda por Profundidad (DFS)!")
            print_path(came_from, current)
            return
        visited.add(tuple(current))
        for neighbor in get_neighbors(current):
            if tuple(neighbor) not in visited and tuple(neighbor) not in came_from:
                came_from[tuple(neighbor)] = current
                stack.append(neighbor)
    print("No se encontró solución con DFS.")

def main():
    print("\n=== Búsqueda por Profundidad (DFS) para el 8 Puzzle ===")
    try:
        start = list(map(int, input("\nIngresa el estado inicial (9 números del 0 al 8, separados por espacios): ").split()))
        if len(start) != 9 or not all(n in range(9) for n in start):
            raise ValueError
    except ValueError:
        print("\nEntrada inválida. Debes ingresar 9 números del 0 al 8 sin repetir.")
        return

    if not is_solvable(start):
        print("\nEste puzzle no es resoluble.")
        return

    depth_first_search(start)

if __name__ == '__main__':
    main()
