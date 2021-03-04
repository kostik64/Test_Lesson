a_int = 7
b_float = 2.7
c_str = "Привет Антон"
d_list = ['b', '3']
e_tuple = ('a', '2')
f_dict = {'Город': 'Саратов', 'Страна': 'Россия'}

plosk_list = [a_int, b_float, c_str, d_list, e_tuple, f_dict]
for i in plosk_list:
    print(f'{i} is {type(i)}')