class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 10
        self.height = 7

    def asphalt_mass(self):
        asphalt_mass = self._length * self._width * self.weight * self.height / 10000
        print(f'Чтобы покрыть всю дорогу нужно {round(asphalt_mass)} кг асфальта')


r = Road(3000, 40)
r.asphalt_mass()