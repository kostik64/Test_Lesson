class MyError(Exception):
    def __init__(self):
        pass


class TypeCheck:
    def __init__(self):
        self.my_list = []

    def check_value(self):
        global user_val
        while True:
            try:
                try:
                    user_val = int(input('Введите числа: '))
                    ex = input(f'Всё good, добавляем "{user_val}" в список. Хотите продолжить? e/d: ').lower()
                    self.my_list.append(user_val)
                    if ex == 'd':
                        print(self.my_list)
                        break
                except ValueError:
                    raise MyError
            except MyError:
                ex = input(f"******* это не число!) Хотите продолжить? e/d: ").lower()
                if ex == 'd':
                    print(self.my_list)
                    break
                else:
                    self.check_value()


a = TypeCheck()
a.check_value()