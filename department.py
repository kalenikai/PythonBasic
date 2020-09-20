# Продолжить работу над первым заданием. 
# Разработать методы, отвечающие за приём оргтехники на склад 
# и передачу в определенное подразделение компании. 
from officeequipment import OfficeEquipment, Computer, Copier, Printer 
from store import Store

class Department:
    def __init__(self, name):
        self.name = name
    items = [] # all devices taken from store


