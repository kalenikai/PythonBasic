# Создать (не программно) текстовый файл со следующим содержимым: 
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
# При этом английские числительные должны заменяться на русские. 
# Новый блок строк должен записываться в новый текстовый файл.
import os
cwd = os.getcwd()
src_dict = {'1':'Один', '2':'Два', '3':'Три', '4':'Четыре'}
words = []
tgt_lines = ''
with open(cwd + '\\' + '4_word_subst_src.txt', 'r', encoding = 'utf-8') as f:
    for row in f.readlines():
        words = row.strip().split(' ')
        tgt_lines += src_dict[words[-1]] + ' - ' + words[-1] + '\n'
with(open(cwd + '\\' + '4_word_subst_tgt.txt', 'w')) as f:
    f.write(tgt_lines)
print(f'Test output:\n{tgt_lines}')
  

