class Regla:
    def __init__(self, condiciones, conclusion):
        self.condiciones = condiciones  # Lista de funciones que reciben hechos
        self.conclusion = conclusion    # Resultado si se cumple la regla

    def evaluar(self, hechos):
        return all(condicion(hechos) for condicion in self.condiciones)


class SistemaExpertoCarreras:
    def __init__(self):
        self.hechos = {}
        self.reglas = []

    def preguntar(self, clave, pregunta):
        respuesta = input(pregunta + " (s/n): ").lower()
        self.hechos[clave] = respuesta == "s"

    def agregar_regla(self, regla):
        self.reglas.append(regla)

    def recomendar(self):
        print("\n--- Recomendación de Carrera ---")
        encontrada = False
        for regla in self.reglas:
            if regla.evaluar(self.hechos):
                print("- " + regla.conclusion)
                encontrada = True
        if not encontrada:
            print("No se encontró una recomendación clara. Considera explorar más tus intereses.")


def main():
    sistema = SistemaExpertoCarreras()

    # Preguntar hechos
    sistema.preguntar("interes_matematicas", "¿Te gustan las matemáticas?")
    sistema.preguntar("interes_programacion", "¿Te interesa la programación?")
    sistema.preguntar("interes_salud", "¿Te interesa la salud y el bienestar?")
    sistema.preguntar("interes_artes", "¿Te gusta el arte o el diseño?")
    sistema.preguntar("interes_negocios", "¿Te interesa el mundo de los negocios?")
    sistema.preguntar("interes_derecho", "¿Te interesa la justicia o las leyes?")
    sistema.preguntar("interes_enseñar", "¿Te gustaría ser maestro o educador?")
    sistema.preguntar("interes_mecanica", "¿Te interesa cómo funcionan las máquinas?")
    sistema.preguntar("interes_animales", "¿Te gustan y te interesa cuidar animales?")
    sistema.preguntar("habilidad_comunicacion", "¿Tienes habilidades para comunicarte con otras personas?")

    # Agregar reglas
    sistema.agregar_regla(Regla(
        [lambda h: h["interes_matematicas"] and h["interes_programacion"]],
        "Podrías estudiar Ingeniería en Sistemas o Ciencias de la Computación."
    ))

    sistema.agregar_regla(Regla(
        [lambda h: h["interes_salud"]],
        "Podrías estudiar Medicina, Enfermería o Nutrición."
    ))

    sistema.agregar_regla(Regla(
        [lambda h: h["interes_artes"]],
        "Podrías estudiar Diseño Gráfico, Artes Visuales o Arquitectura."
    ))

    sistema.agregar_regla(Regla(
        [lambda h: h["interes_negocios"]],
        "Podrías estudiar Administración de Empresas, Contaduría o Marketing."
    ))

    sistema.agregar_regla(Regla(
        [lambda h: h["interes_derecho"]],
        "Podrías estudiar Derecho o Ciencias Políticas."
    ))

    sistema.agregar_regla(Regla(
        [lambda h: h["interes_enseñar"] and h["habilidad_comunicacion"]],
        "Podrías estudiar Educación, Pedagogía o Psicología Educativa."
    ))

    sistema.agregar_regla(Regla(
        [lambda h: h["interes_mecanica"]],
        "Podrías estudiar Ingeniería Mecánica, Mecatrónica o Electrónica."
    ))

    sistema.agregar_regla(Regla(
        [lambda h: h["interes_animales"]],
        "Podrías estudiar Veterinaria o Biología."
    ))

    sistema.agregar_regla(Regla(
        [lambda h: h["interes_programacion"] and h["interes_negocios"]],
        "Podrías estudiar Ingeniería en Software con enfoque empresarial o FinTech."
    ))

    sistema.agregar_regla(Regla(
        [lambda h: h["interes_artes"] and h["habilidad_comunicacion"]],
        "Podrías estudiar Comunicación, Publicidad o Producción Audiovisual."
    ))

    # Ejecutar recomendación
    sistema.recomendar()


if __name__ == "__main__":
    main()
