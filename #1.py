#2 Это номер 2
n = input('Имя')
s = input('Фамилия')
y = int(input('Возраст'))
c = input('Укажи город')
e = input('Напиши емаил')
t = int(input('Напиши номер телефона'))
def my_func (n, s, y, c, e, t):
     return ' '.join([n, s, y, c, e, t])
print(my_func(s, n, y, c, e, t))