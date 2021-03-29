class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма : {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'Произведение : {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'


c_1 = Complex(4, -8)
c_2 = Complex(6, 11)
print(c_1 + c_2)
print(c_1 * c_2)