# Создать текстовый файл (не программно), 
# построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк). 
# Определить, кто из сотрудников имеет оклад менее 20 тыс., 
# вывести фамилии этих сотрудников. 
# Выполнить подсчет средней величины дохода сотрудников.
import os
row_count = 0
cwd = os.getcwd() 
sum_salary = 0.0
with (open(cwd + '\\' + '3_empl_salary.txt', 'r', encoding = 'utf-8')) as f:
    for row in f.readlines():
        row_count += 1
        fname, salary = row.strip().split(' ')
        sum_salary += float(salary)
        if float(salary) < 20000:
            print(f'{fname} has salary {salary}. It is less than 20 000')
print(f'Avarage salary is {sum_salary/row_count}')