# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. 
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список только числами. 
# Класс-исключение должен контролировать типы данных элементов списка.

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

result = []
while True:
    try:
        inp_value = input('Please provide a digit:')
        if inp_value.isdigit() == False:
            raise OwnError("It is not digit. Please retype.")
        else:
            result.append(inp_value)
    except OwnError as err:
        print(err)
    if inp_value == 'stop':
        break


print(result) 



  

