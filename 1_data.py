# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». 
# В рамках класса реализовать два метода. 
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». 
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). 
# Проверить работу полученной структуры на реальных данных.
class Data:
    def __init__(self, dmy):
        self.day, self.month, self.year = dmy.split('-')
    @classmethod
    def cast_to_data(cls, dmy):
        d, m, y = dmy.split('-')
        return  int(d), int(m), int(y)
    @staticmethod
    def check_data(dmy):
        d, m, y = dmy.split('-')
        if int(d) > 31:
            print(f'Value of day cannot be more than 31')
        elif int(m) > 12:
            print(f'Value of month cannot be more than 12')
        elif len(y) != 4:
            print(f'Value of year must have 4 digits')
        else:
            print(f'Provaded string is data')
        


print(Data.cast_to_data('12-12-2020'))
        
print(Data.check_data('12-12-2020'))

print(Data.check_data('32-12-2020'))
