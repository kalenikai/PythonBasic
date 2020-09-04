# Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел. 
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. 
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. 
# Но если вместо числа вводится специальный символ, выполнение программы завершается. 
# Если специальный символ введен после нескольких чисел, 
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

# Реализована защита от "дурака"
# 1. Ввод пробелов после символа
# 2. Ввод контрольного символа без лидирующего пробела
# 3. Ввод в строке любого стмвола вместо числа 

def sum_of_numbers(str):
    numbers = str.split(' ') # populate list
    result = 0.0
    for el in numbers:
        result = result + float(el) 
    return result

# Check if all are digits
def are_all_digits(str):
    numbers = str.split(' ') # populate list
    for el in numbers:
        if el.isdigit():
            continue
        else:
            return False
    return True

result = 0.0
ctrl_symbol = 'q' # Control symbol for exit
while(True):
    inpt_str = input('Please provide a few numbers and pres <Enter> to continue or <q> for exit: ').rstrip()
    last_symbol = inpt_str[-1]
    inpt_str_len = len(inpt_str)
    if (inpt_str_len == 1) and (last_symbol == ctrl_symbol):
        break
    elif (inpt_str_len > 1) and (last_symbol == ctrl_symbol):
        inpt_str = inpt_str[:-1] # drop symbol 'q'
        inpt_str = inpt_str.rstrip() # drop all spaces before 'q'
        if are_all_digits(inpt_str): # Check if all values are digits
            result += sum_of_numbers (inpt_str)
        else:
            print('One or more value are not digit. please correct input' )
            continue 
        break
    else:
        if are_all_digits(inpt_str): # Check if all values are digits
            result += sum_of_numbers (inpt_str)
        else:
            print('One or more value are not digit. please correct input' )
            continue 
print(f'The result is {result}')




