#Пользователь вводит месяц в виде целого числа от 1 до 12. 
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). 
# Напишите решения через list и через dict. 

# Using LIst
month_list = ['January', 'February', 'March', 'April', 'May', 'June' , 'July', 'August', 'September', 'October', 'November', 'December']
season_list = ['Winter', 'Spring', 'Summer', 'Fall']
while(True):
    try:
        month_number = int(input('Please provide a month number from 1 to 12. For exit type 0: '))
    except:
        print('Invalid input. Must be digit')
        continue
    if month_number > 12:
        print('Provided value is incorrect. Please retype')
        continue
    elif month_number == 12:
        print(f'{month_list[month_number-1]} is {season_list[0]}')
        continue
    elif month_number == 0:
        print('Exit. Thanks')
        break
    else:
        print(f'{month_list[month_number-1]} is {season_list[(month_number) // 3]}')


# Using Dict
month_dict = { 
1 : ['January', 'Winter'], 2 : ['February', 'Winter'], 3 : ['March', 'Spring'], 
4 : ['April', 'Spring'], 5 : ['May', 'Spring'], 6 : ['June', 'Summer'], 
7: ['July', 'Summer'], 8 : ['August', 'Summer'], 9 : ['September', 'Fall'],
10 : ['October', 'Fall'], 11 : ['November', 'Fall'], 12 : ['December', 'Winter']}
while(True):
    try:
        month_number = int(input('Please provide a month number from 1 to 12. For exit type 0: '))
    except:
        print('Invalid input. Must be digit')
        continue
    if month_number > 12:
        print('Provided value is incorrect. Please retype')
        continue
    elif month_number == 0:
        print('Exit. Thanks')
        break
    else:
        print(f'{month_dict[month_number][0]} is {month_dict[month_number][1]}')
