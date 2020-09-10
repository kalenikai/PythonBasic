# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
import os

cwd = os.getcwd() 
with (open(cwd + '\\' + '5_count_sum.txt', 'w')) as f:
    inpt_str = input('Please provide a lot of numbers splitted by space and press <Enter>')
    f.writelines(inpt_str)

numbers = []
sumvalue = 0
with (open(cwd + '\\' + '5_count_sum.txt', 'r', encoding = 'utf-8')) as f:
    numbers = f.readline().strip().split(' ')
    for val in numbers:
        sumvalue += float(val)
    print(f'The sum of values is: {sumvalue}')

