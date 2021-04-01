my_f = open('test.txt', 'w')
line = input(' \n')
while line:
    my_f.writelines(line)
    line = input(' \n')
    if not line:
        break

my_f.close()
my_f = open('test.txt', 'r')
c = my_f.readlines()
print(c)
my_f.close()