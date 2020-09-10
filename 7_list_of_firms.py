# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме: 
# название, форма собственности, выручка, издержки. 
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. 
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков). 
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import os
cwd = os.getcwd()
count_firm, sum_profit, f_profit = 0, 0.0, 0.0
dict_firms = {}
list_firms = []

with(open(cwd + '\\' + '7_list_of_firms.txt')) as f:
    for inp_str in f.readlines():
        f_name, f_form, f_revenue, f_costs = inp_str.strip().split(' ')
        f_profit = float(f_revenue) - float(f_costs)
        if  f_profit > 0:
            sum_profit += f_profit
            count_firm += 1
        dict_firms.update({f_name : f_profit}) 
list_firms = [dict_firms, dict(average_profit = round(sum_profit/count_firm, 2))]

print(list_firms)
