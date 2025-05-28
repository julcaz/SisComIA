class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.relaciones = []

    def agregar_relacion(self, tipo, destino):
        self.relaciones.append((tipo, destino))

    def mostrar_relaciones(self):
        for tipo, destino in self.relaciones:
            print(f"{self.nombre} --{tipo}--> {destino.nombre}")

# Crear nodos (conceptos)
canario = Nodo("Canario")
pajaro = Nodo("Pájaro")
animal = Nodo("Animal")
plumas = Nodo("Plumas")
volar = Nodo("Volar")
comida = Nodo("Comida")

# Establecer relaciones (aristas)
canario.agregar_relacion("es_un", pajaro)
pajaro.agregar_relacion("es_un", animal)
canario.agregar_relacion("puede", volar)
canario.agregar_relacion("tiene", plumas)
animal.agregar_relacion("necesita", comida)

# Mostrar la red semántica
print("📚 Red semántica:")
nodos = [canario, pajaro, animal]
for nodo in nodos:
    nodo.mostrar_relaciones()
