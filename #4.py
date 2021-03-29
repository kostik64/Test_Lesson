a_str = input("ВВЕДИТЕ ПРЕДЛОЖЕНИЕ ")
b_word = []
number = 1
for el in range(a_str.count(' ') + 1):
    b_word = a_str.split()
    if len(str(b_word)) <= 10:
        print(f" {number} {b_word [el]}")
        number += 1
    else:
        print(f" {number} {b_word [el] [0:10]}")
        number += 1