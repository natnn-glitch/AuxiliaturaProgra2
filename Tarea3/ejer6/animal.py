class Animal:
    def __init__(self, edad: int, peso: float, especie: str):
        self._edad = edad
        self._peso = peso
        self._especie = especie

    # c. Método respirar() en la clase base
    def respirar(self):
        print(f"[{self._especie}] Acción general: Toma oxígeno de su entorno.")

    # d. Método mover() en la clase base
    def mover(self):
        print(f"[{self._especie}] Acción general: Se desplaza de un lugar a otro.")

    def __str__(self) -> str:
        return f"Especie: {self._especie}, Edad: {self._edad} años, Peso: {self._peso} kg"


class Terrestre(Animal):
    def __init__(self, edad: int, peso: float, especie: str, num_patas: int, tipo_pelaje: str):
        super().__init__(edad, peso, especie)
        self._num_patas = num_patas
        self._tipo_pelaje = tipo_pelaje

    # a. Métodos propios
    def correr(self):
        print(f"El {self._especie} corre a gran velocidad con sus {self._num_patas} patas.")

    def excavar(self):
        print(f"El {self._especie} está excavando un refugio en el suelo.")

    # c. Sobreescritura de respirar()
    def respirar(self):
        super().respirar()
        print(f"   -> Respiración terrestre: Inhala aire mediante sus pulmones.")

    # d. Especialización de mover()
    def mover(self):
        print(f"[{self._especie}] Movimiento: Camina y corre sobre la tierra firme.")

    def __str__(self) -> str:
        return f"Terrestre -> {super().__str__()}, Nro. Patas: {self._num_patas}, Pelaje: {self._tipo_pelaje}"


class Aereo(Animal):
    def __init__(self, edad: int, peso: float, especie: str, envergadura_alas: float, tipo_pico: str):
        super().__init__(edad, peso, especie)
        self._envergadura_alas = envergadura_alas
        self._tipo_pico = tipo_pico

    # a. Métodos propios
    def volar(self):
        print(f"El {self._especie} abre sus alas de {self._envergadura_alas}m de envergadura y vuela.")

    def construirNido(self):
        print(f"El {self._especie} utiliza su pico ({self._tipo_pico}) para tejer su nido.")

    # c. Sobreescritura de respirar()
    def respirar(self):
        super().respirar()
        print(f"   -> Respiración aérea: Utiliza un sistema de pulmones asistido por sacos aéreos.")

    # d. Especialización de mover()
    def mover(self):
        print(f"[{self._especie}] Movimiento: Planea y vuela por los aires.")

    def __str__(self) -> str:
        return f"Aéreo -> {super().__str__()}, Envergadura: {self._envergadura_alas}m, Pico: {self._tipo_pico}"


class Acuatico(Animal):
    def __init__(self, edad: int, peso: float, especie: str, tipo_aletas: str, profundidad_maxima: float):
        super().__init__(edad, peso, especie)
        self._tipo_aletas = tipo_aletas
        self._profundidad_maxima = profundidad_maxima

    # a. Métodos propios
    def nadar(self):
        print(f"El {self._especie} nada velozmente usando sus aletas {self._tipo_aletas}.")

    def sumergirse(self):
        print(f"El {self._especie} se sumerge hasta los {self._profundidad_maxima}m de profundidad.")

    # c. Sobreescritura de respirar()
    def respirar(self):
        super().respirar()
        print(f"   -> Respiración acuática: Extrae oxígeno disuelto en el agua a través de branquias.")

    # d. Especialización de mover()
    def mover(self):
        print(f"[{self._especie}] Movimiento: Se desplaza impulsándose mediante nado acuático.")

    def __str__(self) -> str:
        return f"Acuático -> {super().__str__()}, Aletas: {self._tipo_aletas}, Profundidad Máx: {self._profundidad_maxima}m"


# b. Instanciar los objetos de cada tipo y mostrar sus datos
terrestre1 = Terrestre(4, 42.0, "Puma", 4, "Corto y tupido")
aereo1 = Aereo(2, 1.2, "Halcón", 1.1, "Ganchudo")
acuatico1 = Acuatico(6, 110.0, "Delfín", "Pectorales y dorsal", 300.0)

print("=== Inciso B: Instanciación y datos de cada objeto ===")
print(terrestre1)
print(aereo1)
print(acuatico1)

print("\n=== Inciso C: Prueba del método respirar() ===")
terrestre1.respirar()
aereo1.respirar()
acuatico1.respirar()

print("\n=== Inciso D: Prueba del método mover() ===")
terrestre1.mover()
aereo1.mover()
acuatico1.mover()