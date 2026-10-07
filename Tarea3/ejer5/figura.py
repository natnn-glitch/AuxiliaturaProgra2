import math
from abc import ABC, abstractmethod

# a. Clase base abstracta Figura
class Figura(ABC):
    def __init__(self, color: str):
        self._color = color

    def getColor(self) -> str:
        return self._color

    # Método abstracto que obliga a ser redefinido en subclases
    @abstractmethod
    def obtenerArea(self) -> float:
        pass

    def __str__(self) -> str:
        return f"Figura [Color: {self._color}]"

# b. Sobrescribir el método obtenerArea() en cada subclase
class Cuadrado(Figura):
    def __init__(self, color: str, lado: int):
        super().__init__(color)
        self.__lado = lado

    def obtenerArea(self) -> float:
        return float(self.__lado ** 2)

    def __str__(self) -> str:
        return f"Cuadrado -> Color: {self._color}, Lado: {self.__lado}, Área: {self.obtenerArea():.2f}"

class Triangulo(Figura):
    def __init__(self, color: str, lado1: int, lado2: int, lado3: int):
        super().__init__(color)
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__lado3 = lado3

    def obtenerArea(self) -> float:
        # Cálculo del semiperímetro y fórmula de Herón
        s = (self.__lado1 + self.__lado2 + self.__lado3) / 2.0
        area = math.sqrt(s * (s - self.__lado1) * (s - self.__lado2) * (s - self.__lado3))
        return area

    def __str__(self) -> str:
        return f"Triángulo -> Color: {self._color}, Lados: ({self.__lado1}, {self.__lado2}, {self.__lado3}), Área: {self.obtenerArea():.2f}"

class Redondo(Figura):
    def __init__(self, color: str, radio: int):
        super().__init__(color)
        self.__radio = radio

    def obtenerArea(self) -> float:
        return math.pi * (self.__radio ** 2)

    def __str__(self) -> str:
        return f"Redondo -> Color: {self._color}, Radio: {self.__radio}, Área: {self.obtenerArea():.2f}"


# c. Instanciar 2 objetos de cada subclase y mostrarlos
c1 = Cuadrado("Rojo", 4)
c2 = Cuadrado("Azul", 6)

t1 = Triangulo("Verde", 3, 4, 5)
t2 = Triangulo("Amarillo", 5, 5, 6)

r1 = Redondo("Blanco", 3)
r2 = Redondo("Negro", 5)

print("=== Inciso C: 2 objetos de cada subclase ===")
print(c1)
print(c2)
print(t1)
print(t2)
print(r1)
print(r2)

# d. Dado un Cuadrado y un Triángulo mostrar el color de la figura que tiene mayor área
def mostrar_color_mayor_area(cuadrado: Cuadrado, triangulo: Triangulo):
    area_c = cuadrado.obtenerArea()
    area_t = triangulo.obtenerArea()
    print("\n=== Inciso D: Comparación de Área ===")
    if area_c > area_t:
        print(f"El Cuadrado tiene mayor área ({area_c:.2f} vs {area_t:.2f}). Color: {cuadrado.getColor()}")
    elif area_t > area_c:
        print(f"El Triángulo tiene mayor área ({area_t:.2f} vs {area_c:.2f}). Color: {triangulo.getColor()}")
    else:
        print(f"Ambas figuras tienen la misma área ({area_c:.2f}). Color Cuadrado: {cuadrado.getColor()}, Color Triángulo: {triangulo.getColor()}")

mostrar_color_mayor_area(c1, t1)