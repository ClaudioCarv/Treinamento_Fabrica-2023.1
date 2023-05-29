class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        area = (self.base * self.altura) / 2
        return area


triangulo = Triangulo(5, 4)
area_triangulo = triangulo.calcular_area()
print(f"A área do triângulo é: {area_triangulo}")
