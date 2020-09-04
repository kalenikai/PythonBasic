# Реализовать функцию my_func(), которая принимает три позиционных аргумента, 
# и возвращает сумму наибольших двух аргументов.

def my_func(num1, num2, num3):
    numbers = list([num1, num2, num3])
    numbers.sort()
    return int(numbers[1]) + int(numbers[2])

print(my_func(9, 3, 7))





