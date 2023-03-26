'''Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X'''

from random import randint # не разобрался зачем это

n = int(input('введите кол-во чисел в массиве>>> '))
ArrayNumbers = [randint(0, 100) for _ in range(n)]
print(ArrayNumbers)
n1 = int(input('введите число, к которому надо найти ближайшее в массиве>>> '))
minimumDifference = abs(n1 - ArrayNumbers[0])
closeNumber = ArrayNumbers[0]

for i in ArrayNumbers:
    if abs(n1 - i) < minimumDifference:
        minimumDifference = abs(n1 - i)
        closeNumber = i

print(closeNumber)