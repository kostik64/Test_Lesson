


class Data:
    def __init__(self, day, month, year):
         self.day = day
         self.month = month
         self.year = year
        self.day_month_year = str(day, month, year)

    @classmethod
    def extract(cls, day, month, year):
        my_date = []

        for i in day, month, year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f'Right'
                else:
                    return f'error year'
            else:
                return f'error month'
        else:
            return f'error day'

    def __str__(self):
        return f'now date {Data.extract(self.day_month_year)}'


today = Data('29 - 03 - 2021')
print(today)
print(Data.valid(1, 12, 2021))
print(today.valid(11, 13, 2011))
print(Data.extract('1 - 12 - 2021'))
print(today.extract('1 - 12 - 2021'))
print(Data.valid(1, 112, 2021))