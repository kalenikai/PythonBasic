# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), 
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). 
# Результатом сложения должна быть новая матрица. 

class Matrix:
    def __init__(self, list_of_list):
        self.matrix = list_of_list
        self.columns = len(list_of_list[0])    # number columns
        self.rows = len(list_of_list)          # number nested lists (matrix's rows) 
        if self.rows != 1:                     # check correctness the matrix's structure for two-dimensional matrix
            for el in self.matrix:              
                if len(el) != self.columns:
                    print('Structure data for Matrix is not correct')
                    self.matrix = []         # if structure error, reset matrix
                    self.columns = 0
                    self.rows = 0
                    break
    
    def __str__(self):
        result = ''
        for row in self.matrix:
            for column in row:
                result += str(column) + ','
            result = result[:-1] + '\n'
        return result

    def __add__(self, matrix):
        if self.columns != matrix.columns or self.rows != matrix.rows: # check shapes of matrices, must be the same
            print(f'Shapes of matrices must be the same.')
            print(f'You have {self.columns} x {self.rows} and {matrix.columns} x {matrix.rows}')
            return None
        else:
            resultlist = []
            for i in range(self.rows):
                lst1 = []
                for k in range(self.columns):
                    lst1.append(self.matrix[i][k] + matrix.matrix[i][k])
                resultlist.append(lst1)    
        return Matrix(resultlist)    


# matrices 3 x 4 
list1 = [[1, 2, 3], [4, 5, 6], [4, 5, 6], [7, 8, 9]]
list2 = [[2, 2, 2], [4, 4, 4], [5, 5, 5], [7, 7, 7]]

m1 = Matrix(list1)
m2 = Matrix(list2)
m3 = m1 + m2
print(f'The sum of matrices\n{m1} and\n{m2} is\n{m3}')

# matrices 3 x 3 
list1 = [[1, 2, 3], [4, 5, 6], [4, 5, 6]]
list2 = [[2, 2, 2], [4, 4, 4], [5, 5, 5]]

m1 = Matrix(list1)
m2 = Matrix(list2)
m3 = m1 + m2
print(f'The sum of matrices\n{m1} and\n{m2} is\n{m3}')

# matrices 3 x 1 
list1 = [[1, 2, 3]]
list2 = [[2, 2, 2]]

m1 = Matrix(list1)
m2 = Matrix(list2)
m3 = m1 + m2
print(f'The sum of matrices\n{m1} and\n{m2} is\n{m3}')




