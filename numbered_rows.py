# Пользователь вводит строку из нескольких слов, разделённых пробелами. 
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать. 
# Если в слово длинное, выводить только первые 10 букв в слове

input_str = input('Please provide a few words separatted by the spaces :')
user_list = []
user_list = input_str.rstrip().split(' ')
for ind, el in enumerate(user_list):
    if len(el) > 10:
        result = el[0:10] + '...'
    else:
        result = el 
    print(f'{ind + 1}  {result}')