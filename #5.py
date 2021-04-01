a_list = [8, 6, 4, 5, 2]
print(f"Рейтинг - {a_list}")
digit = int(input("Введите число (18 - выход) "))
while digit != 18:
    for el in range(len(a_list)):
        if a_list[el] == digit:
            a_list.insert(el + 1, digit)
            break
        elif a_list[0] < digit:
            a_list.insert(0, digit)
        elif a_list[-1] > digit:
            a_list.append(digit)
        elif a_list[el] > digit and a_list[el + 1] < digit:
            a_list.insert(el + 1, digit)
    print(f"текущий список - {a_list}")
    digit = int(input("Введите число "))