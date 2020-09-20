# Продолжить работу над первым заданием. 
# Для хранения данных о наименовании и количестве единиц оргтехники, 
# а также других данных, можно использовать любую подходящую структуру, например словарь.
from officeequipment import OfficeEquipment, Computer, Copier, Printer
from myexception import MyException
import random

class Store:
    __item = {'StockNumber' : 0, 'EquipmentType' : '', 'EquipmentObject' : OfficeEquipment}   
    items = []
    
    def put (self, equipment):
        self.__item = {}
        self.__item.update(StockNumber = random.randint(10000, 99999),\
                           EquipmentType = equipment.type, \
                           EquipmentObject = equipment)
        self.items.append(self.__item)
    
    def find_equipment(self, type = 'NA', producer = 'NA'):
        result = []
        if type == 'NA' and producer == 'NA':
            return self.items
        elif type != 'NA' and producer == 'NA':
            for item in self.items:
                if type == item['EquipmentType']:
                    result.append(item)
        elif type == 'NA' and producer != 'NA':
            for item in self.items:
                if producer == item['EquipmentObject'].producer:
                    result.append(item)
        elif type != 'NA' and producer != 'NA':
            for item in self.items:
                if producer == item['EquipmentObject'].producer and type == item['EquipmentType']:
                    result.append(item)
        return result

    def calc_equipment(self, type = 'NA', producer = 'NA'):
        result = self.find_equipment(type, producer)  
        print(f'Total equipments type {type} and producer {producer} is {len(result)}')  
    
    def issue_equipment(self, department, type, producer = 'NA'):
        result = OfficeEquipment()
        retval = False
        try: 
            result = self.find_equipment(type, producer)
            if len(result) == 0:
                raise MyException("\nThere are no requested devices.\n")
            for dev in result:
                if dev['EquipmentObject'].location == 'Store':
                    dev['EquipmentObject'].location = department.name
                    department.items.append(dev)
                    retval = True
                    return retval
            if retval == False:
                raise MyException("\nError issuing. There are no devices in store.\n")
        except MyException as err:
            print(err)             
    
    def find_equipment_by_department(self, type = 'NA', producer = 'NA', department = 'NA'):
        result = [] 
        tmp = self.find_equipment(type, producer)
        for dev in tmp:
            if dev['EquipmentObject'].location == department:
                result.append(dev)
        return result        
    




         

# Test classes
if __name__ == "__main__":
    comp1 = Computer(12, 'HP', 4, 8, 1000)
    comp2 = Computer(5, 'Lenovo', 4, 8, 1000)
    prn1 = Printer(23, 'HP')
    cpr1 = Copier(12, 'Xerox', 'A3')

    store = Store()
    store.put(comp1)
    store.put(comp2)
    store.put(prn1)
    store.put(cpr1)

    items = [] 
    items = store.find_equipment(type = 'Printer', producer = 'HP')
    for item in items:
        print(item)
    
    store.calc_equipment(type = 'Printer', producer = 'HP')
