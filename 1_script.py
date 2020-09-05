# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. 
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия. 
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv

script_name, production, wage_per_hour, bonus = argv

print("Имя скрипта: ", script_name)
print("Выработка в часах: ", production)
print("Ставка часа: ", wage_per_hour)
print("Премия: ", bonus)
print(f'Итого заработная плата составит: {(float(production) * float(wage_per_hour)) + float(bonus)} руб.')
