# Реализовать базовый класс Worker (работник), в котором определить атрибуты: 
# name, surname, position (должность), income (доход). 
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, 
# например, {"wage": wage, "bonus": bonus}. 
# Создать класс Position (должность) на базе класса Worker. 
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) 
# и дохода с учетом премии (get_total_income). 
# Проверить работу примера на реальных данных 
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, 
# вызвать методы экземпляров).

class Worker:
    def __init__ (self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = dict(wage = wage, bonus = bonus)

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        self.worker = Worker(name, surname, position, wage, bonus)
    def get_full_name(self):
        return self.worker.name + ' ' + self.worker.surname
    def get_total_income(self):
        return self.worker._income['wage'] + self.worker._income['bonus']    
    def get_position(self):
        return self.worker.position

# Create object 
pos = Position('John', 'Yellow', 'Mgr', 1000, 300)

print(f'Full name is: {pos.get_full_name()}')
print(f'Income is: {pos.get_total_income()}')
print(f'Position is: {pos.get_position()}')

