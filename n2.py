class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


def div():
    try:
        user_num_1 = int(input(' делимое: '))
        user_num_2 = int(input(' делитель: '))
        if user_num_2 == 0:
            raise OwnError("Ты чо дурак?)")
        else:
            res = user_num_1 / user_num_2
            return res
    except ValueError:
        return "Вы ввели не число"
    except OwnError as err:
        return err


print(div())