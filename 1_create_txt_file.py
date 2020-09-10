# Создать программно файл в текстовом формате, 
# записать в него построчно данные, вводимые пользователем. 
# Об окончании ввода данных свидетельствует пустая строка.
with (open('1_create_txt_file.txt', 'w')) as f:
    while(True):
        inpt_str = input('Please provide any text and press <Enter>. To cancel press <Enter>:')
        if inpt_str != '':
            f.writelines(inpt_str + '\n')
        else:
            break


