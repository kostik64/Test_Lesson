class Office:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.items = {'Модель ': self.name, 'Цена за 1': self.price, 'Количество': self.quantity}

    def income(self):
        try:
            name = input(f'Название: ')
            price = int(input(f' цена за ед: '))
            quantity = int(input(f' количество: '))
            item = {'Модель ': name, 'Цена за 1': price, 'Количество': quantity}
            self.items.update(item)
            print(self.items)
        except ValueError:
            print('Неа, недопущу!')


class Printer(Office):
    pass


class Scan(Office):
    pass


class Kserox(Office):
    pass


p = Printer('Какой-то принтер', 1, 400)
s = Scan('Какой-то сканнер', 50000, 1)
x = Kserox('Какой-то ксеокс', 8000, 1)
p.income()
s.income()
x.income()