from utils_8puzzle import *

import heapq

def heuristic(state):
    distance = 0
    for i, val in enumerate(state):
        if val != 0:
            goal_pos = GOAL_STATE.index(val)
            current_row, current_col = divmod(i, 3)
            goal_row, goal_col = divmod(goal_pos, 3)
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance

def a_star_search(start):
    open_set = []
    heapq.heappush(open_set, (heuristic(start), 0, start))
    came_from = {tuple(start): None}
    g_score = {tuple(start): 0}
    closed_set = set()

    while open_set:
        _, cost, current = heapq.heappop(open_set)
        if current == GOAL_STATE:
            print("\n¡Solución encontrada con Búsqueda Heurística (A*)!")
            print_path(came_from, current)
            return
        closed_set.add(tuple(current))

        for neighbor in get_neighbors(current):
            tentative_g_score = g_score[tuple(current)] + 1
            neighbor_t = tuple(neighbor)
            if neighbor_t in closed_set:
                continue
            if neighbor_t not in g_score or tentative_g_score < g_score[neighbor_t]:
                came_from[neighbor_t] = current
                g_score[neighbor_t] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor)
                heapq.heappush(open_set, (f_score, tentative_g_score, neighbor))
    print("No se encontró solución con A*.")

def main():
    print("\n=== Búsqueda Heurística (A*) para el 8 Puzzle ===")
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

    a_star_search(start)

if __name__ == '__main__':
    main()
