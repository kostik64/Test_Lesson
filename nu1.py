def simple_calc():
    a = float(input('количество отработанных часов : '))
    b= float(input('суммы оплаты труда за 1 час : '))
    c = float(input(' размер премии - '))
    d = a * b
    return d + c
print((f'Размер заработной платы составил: {simple_calc() }'))
