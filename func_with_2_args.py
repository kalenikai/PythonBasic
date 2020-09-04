# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. 
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def my_div(num1, num2):
    try:
        return(num1 / num2)
    except ZeroDivisionError:
        print(f'The second number is zero. Please input correct number')

while(True):
    try:
        num1 =  int(input('Plese provide the first number: '))
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        continue
    try:
        num2 =  int(input('Plese provide the second number: '))
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        continue
    cntrl_symb = input('To continue press "y", for exit pres "n"')
    if cntrl_symb.upper() ==  'N':
        print('Exit')
        break
    elif my_div(num1, num2) == None:
        print (f'The result of division is not defined')
        continue
    else:
        print (f'The result of division is {round(my_div(num1, num2), 2)}')