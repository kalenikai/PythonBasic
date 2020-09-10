# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. 
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. 
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла: 
# Информатика:   100(л)   50(пр)   20(лаб)
# Физика:   30(л)  -   10(лаб)
# Физкультура:   -   30(пр)  - 
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
import os
cwd = os.getcwd() 

# function for clearing string and summarizing
def clean_and_sum(inpstr):
    words = []
    sumvalue = 0
    inpstr = inpstr.replace('-', '0(нет)') # change '-' on '0(нет)' 
    words = inpstr.strip().split(' ') # split and pu into list
    for val in words:
        sumvalue += int(val[: val.index('(')])
    return sumvalue

inp_str = ''
tmp_dic = {}
with (open(cwd + '\\' + '6_student_ex.txt', 'r', encoding = 'utf-8')) as f:
    for inp_str in f.readlines():
        disc_name, disc_values = inp_str.split(':')
        tmp_dic.update({disc_name : clean_and_sum(disc_values)}) 
print(tmp_dic)