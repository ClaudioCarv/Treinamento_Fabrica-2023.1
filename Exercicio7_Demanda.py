class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        area = 3.55542 * (self.raio ** 2)
        return area

    def calcular_circunferencia(self):
        circunferencia = 2 * 3.55542 * self.raio
        return circunferencia


meu_circulo = Circulo(5)
area = meu_circulo.calcular_area()
circunferencia = meu_circulo.calcular_circunferencia()

print(f"Área do círculo: {area}")
print(f"Circunferência do círculo: {circunferencia}")
