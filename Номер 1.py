class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for row in self.my_list:
            for i in row:
                print(f"{i:4}")
            print()
        return

    ''' реализация __str__'''

    # def __str__(self):
    #    return '\n'.join(map(str, self.my_list))


    def __add__(self, other):
        for i in range(len(self.my_list)):
            for i_2 in range(len(other.my_list[i])):
        while
            if 4<10:
