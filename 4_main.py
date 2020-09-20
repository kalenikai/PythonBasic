# Продолжить работу над первым заданием. 
# Это главный модуль, предназначенный для тестирования

from officeequipment import OfficeEquipment, Computer, Copier, Printer 
from store import Store
from department import Department
from myexception import MyException


comp1 = Computer(12, 'HP', 4, 8, 1000)
comp2 = Computer(5, 'Lenovo', 4, 8, 1000)
prn1 = Printer(23, 'HP')
cpr1 = Copier(12, 'Xerox', 'A3')

store = Store()
store.put(comp1)
store.put(comp2)
store.put(prn1)
store.put(cpr1)
    
# Create departments
dep1 = Department('DevOps')
# Issue device to department
if (store.issue_equipment(dep1, 'Computer')):
    print(f'Equipmrnt for {dep1.name} is issued')
if (store.issue_equipment(dep1, 'Computer')):
    print(f'Equipmrnt for {dep1.name} is issued')
# It must me error. There are no devices in store.
if (not store.issue_equipment(dep1, 'Computer')):
    print(f'Equipment for {dep1.name} is not issued\n\n')
# Find devices issued to department DevOps
items = store.find_equipment_by_department(department = 'DevOps')
for item in items:
    print(f'The department {dep1.name} got this devices {item}')    
print()

# Create departments
dep2 = Department('ITG')
# Issue device to department
if (store.issue_equipment(dep2, 'Printer')):
    print(f'Equipmrnt for {dep2.name} is issued')
# Find devices issued to department ITG
items = store.find_equipment_by_department(department = 'ITG')
for item in items:
    print(f'The department {dep2.name} got this devices {item}')    
print()

# Check all devices
items = [] 
items = store.find_equipment()
for item in items:
    print(f'Device {item["EquipmentObject"].type}, probuced by {item["EquipmentObject"].producer}, issued to {item["EquipmentObject"].location}')
print()    

# Check devices type <Computer>    
items = [] 
items = store.find_equipment(type = 'Computer')
for item in items:
    print(f'Device {item["EquipmentObject"].type}, probuced by {item["EquipmentObject"].producer}, issued to {item["EquipmentObject"].location}')

