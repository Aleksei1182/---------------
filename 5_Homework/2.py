'''Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных
 чисел. Из всех арифметических операций допускаются только +1 и -1. 
 Также нельзя использовать циклы.
*Пример:*
2 2
    4'''

def Sum(a, b):
    if b == 0:
        return a
    else:
        return 1 + Sum(a, b-1)

a1 = int(input('Введите число: '))
b1 = int(input('Введите число: '))

print(Sum(a1, b1))