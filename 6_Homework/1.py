'''Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
Ввод: 7 2 5
Вывод: 7 9 11 13 15'''

def Arithmetic_progression (a, b, c):
    list = [a]
    for i in range(c-1):
        a = a + b
        list.append(a)
    print(list)
    

a1 = int(input('введите начальное число: '))
b1 = int(input('Введите разность: '))
c1 = int(input('Введите кол-во элементов: '))

Arithmetic_progression (a1, b1, c1)