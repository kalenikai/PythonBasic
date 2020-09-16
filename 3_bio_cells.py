# Реализовать программу работы с органическими клетками, состоящими из ячеек. 
# Необходимо создать класс Клетка. 
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). 
# В классе должны быть реализованы методы перегрузки арифметических операторов: 
# сложение (__add__()), 
# вычитание (__sub__()), 
# умножение (__mul__()), 
# деление (__truediv__()). 
# Данные методы должны применяться только к клеткам
# и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. 
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. 
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

class BioCell:
    def __init__(self, slots):
        self.slots = slots
    def __add__(self, biocell):
        return self.slots + biocell.slots
    def __sub__(self, biocell):
        if self.slots - biocell.slots > 0:
           return self.slots - biocell.slots
        else:
            print(f'Error. Left cell has less slots than right')
            return None    
    def __mul__(self, biocell):
        return abs(self.slots * biocell.slots)
    def __truediv__(self, biocell):
        return (self.slots + biocell.slots) // 2
    def make_order(self, columns):
        return (self.slots // columns) * (columns * '*' + '\n') + (self.slots % columns) * '*' 


bc1 = BioCell(28)
bc2 = BioCell(5)

print(f'Sum of two cells is {bc1 + bc2}')
print(f'Difference of two cells is {bc1 - bc2}')
print(f'Production of two cells is {bc1 * bc2}')
print(f'Dividing of two cells is {bc1 / bc2}')

print(bc1.make_order(6))
print()
print(bc1.make_order(5))

