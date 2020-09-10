# Создать текстовый файл (не программно), 
# сохранить в нем несколько строк, 
# выполнить подсчет количества строк, количества слов в каждой строке.
import os
row_count = 0
words = []
cwd = os.getcwd() 
with (open(cwd + '\\' + '2_text.txt', 'r', encoding = 'utf-8')) as f:
    for row in f.readlines():
        row_count += 1
        words = row.strip().split(' ')
        print(f'Row number {row_count} words {len(words)}')


