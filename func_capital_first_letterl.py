# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой. 
# Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. 
# Каждое слово состоит из латинских букв в нижнем регистре. 
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. 
# Необходимо использовать написанную ранее функцию int_func().

def int_func(word):
    return word.title()

words = []
inpt_str = input('Please prodive words separeted by space and pres <Enter>: ').rstrip()
words = inpt_str.split(' ')

result = ''
for word in words:
    result += ' ' + int_func(word)
print(result)
