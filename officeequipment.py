# Начните работу над проектом «Склад оргтехники». 
# Создайте класс, описывающий склад. 
# А также класс «Оргтехника», который будет базовым для классов-наследников. 
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
# В базовом классе определить параметры, общие для приведенных типов. 
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники. 
import random
from abc import ABC, abstractmethod

@abstractmethod
class OfficeEquipment(ABC):
    def __init__(self, type = 'NA', weight = 0, producer = 'NA'):
        self.type = type
        self.weight = weight
        self.producer = producer
        self.location = 'Store' # All equipment first go to store
    def __str__(self):
        pass

class Computer(OfficeEquipment):
    def __init__(self, weight, producer, cpu, ram_size, disk_size):
        super().__init__( 'Computer', weight, producer)
        self.cpu = cpu
        self.ram_size = ram_size
        self.disk_size = disk_size

    def __str__(self):
        return 'Computer Weight:' + str(self.weight) + '. Produced by :' + self.producer + '. Numper CPUs: ' + str(self.cpu) + '. RAM size :' + str(self.ram_size) + '. Disks size :' + str(self.disk_size)

class Printer(OfficeEquipment):
    def __init__(self, weight, producer, page_size = 'A4', print_techn = 'Laser', color = 'no'):
        super().__init__('Printer', weight, producer) 
        self.print_techn = print_techn
        self.color = color.upper()
        self.page_size = page_size
        if self.color != 'YES' and self.color != 'NO':
            print('Provide correct value <Yes> or <No>')
            self.print_techn = None
            self.color = None
            self.page_size = None

    def __str__(self):
        return 'Printer Weight:' + str(self.weight) + '. Produced by :' + self.producer + '. Print technology: ' + str(self.print_techn) + '. Color :' + self.color + '. Max Page size :' + self.page_size

class Copier(OfficeEquipment):
    def __init__(self, weight, producer, page_size = 'A4', copier_techn = 'Laser', color = 'No'):
        super().__init__('Copier', weight, producer) 
        self.copier_techn = copier_techn
        self.color = color.upper()
        self.page_size = page_size
        if self.color != 'YES' and self.color != 'NO':
            print('Provide correct value <Yes> or <No>')
            self.copier_techn = None
            self.color = None
            self.page_size = None

    def __str__(self):
        return 'Copier Weight:' + str(self.weight) + '. Produced by :' + self.producer + '. Copying technology: ' + str(self.copier_techn) + '. Color :' + self.color + '. Max Page size :' + str(self.page_size)


# Test classes
if __name__ == "__main__":
    comp = Computer(12, 'HP', 4, 4, 500)
    print(comp)
    prn = Printer(10, 'Samsung')
    print(prn)
    cop = Copier(24, 'Xerox', 'A3')
    print(cop) 


