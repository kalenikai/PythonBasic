# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. 
# У пользователя необходимо запрашивать новый элемент рейтинга. 
# Если в рейтинге существуют элементы с одинаковыми значениями, 
# то новый элемент с тем же значением должен разместиться после них.

my_rate = [7, 5, 3, 3, 2]
while(True):
    try:
        input_value = int(input('Please provide a integer value. For exit type 0: '))
    except:
        print('Invalid input. Must be digit')
        continue
    if input_value == 0:
        print('Exit. Bye')
        break
    max_index = len(my_rate) - 1
    print(f'The rate before is {my_rate}')
    for indx, el in enumerate(my_rate):
        if input_value > el: 
            my_rate.insert(indx, input_value)
            break
        elif input_value <= el and indx == max_index:
            my_rate.append(input_value)
            break
        else:
            continue
    print (f'The rate after is {my_rate}')
    