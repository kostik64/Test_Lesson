# это номер 5
def my_sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Введи число или нажми энтер, для выхода - ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'Enter':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'В данный момент число равно {sum_res}')
    print(f'Твой конечный результат {sum_res}')


my_sum()