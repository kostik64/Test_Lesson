def summary():
    try:
        with open('file_5.txt', 'w+') as file_obj:
            line = input('Цифры через пробел \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка')
    except ValueError:
        print('Неверный номер')
summary()