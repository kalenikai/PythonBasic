# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. 
# Проверьте его работу на данных, вводимых пользователем. 
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой

class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt

while (True):
    try:
        inp_value_1 = int(input('Please provide the first digit'))
        inp_value_2 = int(input('Please provide the second digit'))
        if inp_value_2 == 0:
            raise MyException('Provided value is zero. Please correct.')
        else:
            break
    except ValueError:
        print('It is not digit')
    except MyException as err:
        print(err)    

print (f'The resul is {inp_value_1 / inp_value_2}')

