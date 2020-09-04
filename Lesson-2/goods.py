# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. 
# Каждый кортеж хранит информацию об отдельном товаре. 
# В кортеже должно быть два элемента — номер товара и словарь с параметрами 
# (характеристиками товара: название, цена, количество, единица измерения).
# Необходимо собрать аналитику о товарах. 
# Реализовать словарь, в котором каждый ключ — характеристика товара, например название, 
# а значение — список значений-характеристик, например список названий товаров.
# goods = [
    # (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'ед': 'шт.'}),
    # (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'ед': 'шт.'}),
    # (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'ед': 'шт.'})]

indx = 1
goods = []
print(type(goods))
end_flag = ''
while (end_flag != 'Q'):
    tmp_dict = {}
    tmp_set = ()
    name = input('Please provide the goods name: ')
    try:
        price = int(input('Please provide the goods price: '))
    except:
        print('Invalid input. Must be digit')
        continue
    try:
        amount = int(input('Please provide the goods amoutn: '))
    except:
        print('Invalid input. Must be digit')
        continue
    unit = input('Please provide the goods unit: ')
    end_flag = input('Fo finishing type "Q": ')
    tmp_dict.update(название = name, цена = price, количество = amount, ед = unit)
    tmp_set = (indx, tmp_dict)
    goods.append(tmp_set)
    indx += 1


# resulting dict
result = {}
# temporary lists
name_list = []
price_list = []
num_list = []
it_list = []
# forming result dict
for el in goods:
    name_list.append(el[1]['название'])
    price_list.append(el[1]['цена'])
    num_list.append(el[1]['количество'])
    it_list.append(el[1]['ед'])
result.update(название = name_list, цена = price_list, количество = num_list, ед = it_list)
print(result)

