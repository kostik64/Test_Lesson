from itertools import count

for el in count(int(input('Число '))):
    print(el)

from itertools import cycle

my_list = [False, 'Bmw', 777]
for el in cycle(my_list):
    print(el)