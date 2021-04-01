class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Рисую'


class Pen(Stationery):
    def draw(self):
        return f'Рисую {self.title}'


class Pencil(Stationery):
    def draw(self):
        return f'Рисую {self.title}'


class Handle(Stationery):
    def draw(self):
        return f'Рисую {self.title}'


pen = Pen('ручкой')
print(pen.draw())
pencil = Pencil('карандашом')
print(pencil.draw())
handle = Handle('маркером')
print(handle.draw())