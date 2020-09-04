# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. 
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def full_user_info (fname, lname, birthdate, homecity, email, phone):
    return fname.title() + ' ' + lname.title() + ' ' + birthdate + ' ' + homecity + ' ' + email + ' ' + phone

fname = 'John'
lname = 'McCloud'
birthdate = '12/31/2017'
homecity = 'Seattle'
email = 'jmcd@test.com'
phone = '+1 890 567 3456'

print (full_user_info(fname, lname, birthdate, homecity, email, phone))
