class Circulo:
    PI = 3.1416

    def __init__(self, radio):
        self.radio = radio

    def circunferencia(self):
        return 2 * self.PI * self.radio

    def area(self):
        return self.PI * self.radio * self.radio


if __name__ == "__main___":
    instancia_circulo = Circulo(10)
    print(f"La cicurferencia es: {instancia_circulo.circunferencia()}")
    print(f"El area es: {instancia_circulo.area()}")
