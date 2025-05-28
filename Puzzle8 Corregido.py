import heapq
from collections import deque

GOAL_STATE = [1, 2, 3, 4, 5, 6, 7, 8, 0]
MOVES = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}

def get_neighbors(state):
    neighbors = []
    zero_pos = state.index(0)
    for move in MOVES[zero_pos]:
        new_state = state[:]
        new_state[zero_pos], new_state[move] = new_state[move], new_state[zero_pos]
        neighbors.append(new_state)
    return neighbors

def is_solvable(state):
    inv_count = 0
    for i in range(8):
        for j in range(i+1, 9):
            if state[i] and state[j] and state[i] > state[j]:
                inv_count += 1
    return inv_count % 2 == 0

def print_path(came_from, end):
    path = []
    while end:
        path.append(end)
        end = came_from[tuple(end)]
    path.reverse()
    for step in path:
        print_board(step)
        print()

def print_board(state):
    for i in range(0, 9, 3):
        print(state[i], state[i+1], state[i+2])

def breadth_first_search(start):
    visited = set()
    queue = deque([start])
    came_from = {tuple(start): None}

    while queue:
        current = queue.popleft()
        if current == GOAL_STATE:
            print("\n¡Solución encontrada con BFS!")
            print_path(came_from, current)
            return
        visited.add(tuple(current))
        for neighbor in get_neighbors(current):
            if tuple(neighbor) not in visited and tuple(neighbor) not in came_from:
                came_from[tuple(neighbor)] = current
                queue.append(neighbor)
    print("No se encontró solución con BFS.")

def depth_first_search(start):
    visited = set()
    stack = [start]
    came_from = {tuple(start): None}

    while stack:
        current = stack.pop()
        if current == GOAL_STATE:
            print("\n¡Solución encontrada con DFS!")
            print_path(came_from, current)
            return
        visited.add(tuple(current))
        for neighbor in get_neighbors(current):
            if tuple(neighbor) not in visited and tuple(neighbor) not in came_from:
                came_from[tuple(neighbor)] = current
                stack.append(neighbor)
    print("No se encontró solución con DFS.")

def manhattan(state):
    distance = 0
    for i, val in enumerate(state):
        if val == 0:
            continue
        goal_pos = GOAL_STATE.index(val)
        distance += abs(i // 3 - goal_pos // 3) + abs(i % 3 - goal_pos % 3)
    return distance

def a_star_search(start):
    open_set = [(manhattan(start), 0, start)]
    came_from = {tuple(start): None}
    g_score = {tuple(start): 0}
    visited = set()

    while open_set:
        _, cost, current = heapq.heappop(open_set)
        if current == GOAL_STATE:
            print("\n¡Solución encontrada con A* (heurística de Manhattan)!")
            print_path(came_from, current)
            return
        visited.add(tuple(current))
        for neighbor in get_neighbors(current):
            t_neighbor = tuple(neighbor)
            temp_g = g_score[tuple(current)] + 1
            if t_neighbor not in g_score or temp_g < g_score[t_neighbor]:
                g_score[t_neighbor] = temp_g
                priority = temp_g + manhattan(neighbor)
                heapq.heappush(open_set, (priority, temp_g, neighbor))
                came_from[t_neighbor] = current
    print("No se encontró solución con A*.")

def main():
    print("\n=== 8 Puzzle Solver ===")
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

    print("\nElige el algoritmo de búsqueda:")
    print("1. Búsqueda por Anchura (BFS)")
    print("2. Búsqueda por Profundidad (DFS)")
    print("3. Búsqueda Heurística (A* con Manhattan)")

    choice = input("\nIngresa el número de la opción: ")

    if choice == '1':
        breadth_first_search(start)
    elif choice == '2':
        depth_first_search(start)
    elif choice == '3':
        a_star_search(start)
    else:
        print("\nOpción inválida.")

if __name__ == '__main__':
    main()
8