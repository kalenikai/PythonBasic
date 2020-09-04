# Для списка реализовать обмен значений соседних элементов, т.е. 
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. 
# При нечетном количестве элементов последний сохранить на своем месте. 
# Для заполнения списка элементов необходимо использовать функцию input().

# Using other List
my_list = []
dest_list = []
while (True):
    my_value = input('Please provide a value. For ending press Enter: ')
    if my_value == '':
        break
    my_list.append(my_value)
for i in range(len(my_list)):
    if i % 2:
        dest_list.insert(i-1, my_list[i])
    else:
        dest_list.insert(i+1, my_list[i])
print(f'Source list {my_list}')
print(f'Result list {dest_list}')


# Using the same List and .pop()
my_list = []
while (True):
    my_value = input('Please provide a value. For ending press Enter: ')
    if my_value == '':
        break
    my_list.append(my_value)
print(f'Source list {my_list}')
for i in range(len(my_list)):
    if i % 2:
        my_list.insert(i-1, my_list.pop(i))
    else:
        continue
print(f'Result list {my_list}')