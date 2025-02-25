
package inteligencia.artificial;

import java.util.*;

// Clase Nodo
class Nodo {
    int[][] estado;
    Nodo padre;
    int costo; 

    public Nodo(int[][] estado, Nodo padre, int costo) {
        this.estado = Puzzle8.copiarMatriz(estado);
        this.padre = padre;
        this.costo = costo;
    }
}

// Clase principal Puzzle8
public class Puzzle8 {
    private static final int[][] OBJETIVO = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 0}
    };

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Ingrese el estado inicial del rompecabezas (3x3), usando 0 para el espacio vacío:");
        int[][] estadoInicial = new int[3][3];

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                estadoInicial[i][j] = sc.nextInt();
            }
        }

        System.out.println("Seleccione el método de búsqueda:");
        System.out.println("1. Búsqueda en Anchura (BFS)");
        System.out.println("2. Búsqueda de Costo Uniforme (UCS)");
        System.out.println("3. Búsqueda en Profundidad Iterativa (IDDFS)");
        System.out.println("4. Búsqueda Bidireccional");

        int opcion = sc.nextInt();
        switch (opcion) {
            case 1:
                System.out.println("Ejecutando Búsqueda en Anchura (BFS)...");
                bfs(estadoInicial);
                break;
            case 2:
                System.out.println("Ejecutando Búsqueda de Costo Uniforme (UCS)...");
                ucs(estadoInicial);
                break;
            case 3:
                System.out.println("Ejecutando Búsqueda en Profundidad Iterativa (IDDFS)...");
                iddfs(estadoInicial);
                break;
            case 4:
                System.out.println("Ejecutando Búsqueda Bidireccional...");
                bidireccional(estadoInicial);
                break;
            default:
                System.out.println("Opción no válida.");
        }
    }

    private static void bfs(int[][] estadoInicial) {
        Queue<Nodo> frontera = new LinkedList<>();
        Set<String> visitados = new HashSet<>();

        Nodo nodoInicial = new Nodo(estadoInicial, null, 0);
        frontera.add(nodoInicial);
        visitados.add(Arrays.deepToString(nodoInicial.estado));

        while (!frontera.isEmpty()) {
            Nodo nodoActual = frontera.poll();

            if (esObjetivo(nodoActual.estado)) {
                System.out.println("¡Solución encontrada!");
                imprimirCamino(nodoActual);
                return;
            }

            for (int[][] sucesor : generarSucesores(nodoActual.estado)) {
                String claveEstado = Arrays.deepToString(sucesor);
                if (!visitados.contains(claveEstado)) {
                    frontera.add(new Nodo(sucesor, nodoActual, 0));
                    visitados.add(claveEstado);
                }
            }
        }
        System.out.println("No se encontró solución.");
    }

    private static void ucs(int[][] estadoInicial) {
        PriorityQueue<Nodo> frontera = new PriorityQueue<>(Comparator.comparingInt(n -> n.costo));
        Set<String> visitados = new HashSet<>();

        Nodo nodoInicial = new Nodo(estadoInicial, null, 0);
        frontera.add(nodoInicial);
        visitados.add(Arrays.deepToString(nodoInicial.estado));

        while (!frontera.isEmpty()) {
            Nodo nodoActual = frontera.poll();

            if (esObjetivo(nodoActual.estado)) {
                System.out.println("¡Solución encontrada!");
                imprimirCamino(nodoActual);
                return;
            }

            for (int[][] sucesor : generarSucesores(nodoActual.estado)) {
                String claveEstado = Arrays.deepToString(sucesor);
                if (!visitados.contains(claveEstado)) {
                    frontera.add(new Nodo(sucesor, nodoActual, nodoActual.costo + 1));
                    visitados.add(claveEstado);
                }
            }
        }
        System.out.println("No se encontró solución.");
    }

    private static void iddfs(int[][] estadoInicial) {
        int profundidadMax = 20;
        for (int profundidad = 0; profundidad <= profundidadMax; profundidad++) {
            Set<String> visitados = new HashSet<>();
            if (dfsLimitado(new Nodo(estadoInicial, null, 0), profundidad, visitados)) {
                return;
            }
        }
        System.out.println("No se encontró solución.");
    }

    private static boolean dfsLimitado(Nodo nodo, int limite, Set<String> visitados) {
        if (esObjetivo(nodo.estado)) {
            System.out.println("¡Solución encontrada!");
            imprimirCamino(nodo);
            return true;
        }
        if (limite == 0) return false;

        visitados.add(Arrays.deepToString(nodo.estado));

        for (int[][] sucesor : generarSucesores(nodo.estado)) {
            String claveEstado = Arrays.deepToString(sucesor);
            if (!visitados.contains(claveEstado)) {
                if (dfsLimitado(new Nodo(sucesor, nodo, 0), limite - 1, visitados)) {
                    return true;
                }
            }
        }
        return false;
    }

    private static void bidireccional(int[][] estadoInicial) {
        System.out.println("Método de búsqueda bidireccional aún no implementado.");
    }

    private static boolean esObjetivo(int[][] estado) {
        return Arrays.deepEquals(estado, OBJETIVO);
    }

    private static List<int[][]> generarSucesores(int[][] estado) {
        List<int[][]> sucesores = new ArrayList<>();
        int fila = -1, columna = -1;

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (estado[i][j] == 0) {
                    fila = i;
                    columna = j;
                    break;
                }
            }
        }

        int[][] movimientos = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        for (int[] mov : movimientos) {
            int nuevaFila = fila + mov[0];
            int nuevaColumna = columna + mov[1];

            if (nuevaFila >= 0 && nuevaFila < 3 && nuevaColumna >= 0 && nuevaColumna < 3) {
                int[][] nuevoEstado = copiarMatriz(estado);
                nuevoEstado[fila][columna] = nuevoEstado[nuevaFila][nuevaColumna];
                nuevoEstado[nuevaFila][nuevaColumna] = 0;
                sucesores.add(nuevoEstado);
            }
        }
        return sucesores;
    }

    public static int[][] copiarMatriz(int[][] matriz) {
        int[][] copia = new int[3][3];
        for (int i = 0; i < 3; i++) {
            copia[i] = matriz[i].clone();
        }
        return copia;
    }

    private static void imprimirCamino(Nodo nodo) {
        throw new UnsupportedOperationException("Not supported yet."); // Generated from nbfs://nbhost/SystemFileSystem/Templates/Classes/Code/GeneratedMethodBody
    }
}
