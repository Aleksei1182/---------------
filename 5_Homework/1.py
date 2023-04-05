'''Напишите программу, которая на вход принимает два числа A и B, 
и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 '''

def Exponentiation(a, b):
    if b == 1:
        return a
    if b == 0:
        return 1
    else:
        return a * Exponentiation(a, b-1)
    


a1 = int(input('введите число: '))
b1 = int(input('Введите степень числа: '))

print(Exponentiation(a1, b1))