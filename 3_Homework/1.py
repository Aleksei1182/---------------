'''Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X'''

from random import randint # не разобрался зачем это

n = int(input('введите кол-во чисел в массиве>>> '))
ArrayNumbers = [randint(0, 10) for _ in range(n)]
print(ArrayNumbers)
n1 = int(input('введите число, по котрому нужно определить сколько раз оно встречается в массиве>>> '))
quantity = 0
for i in ArrayNumbers:
    if i == n1:
        quantity += 1
print(quantity)