'''Требуется определить, можно ли от шоколадки размером n
× m долек отломить k долек, если разрешается сделать один разлом по
прямой между дольками (то есть разломить шоколадку на два
прямоугольника).
Пример
3 2 4 -> yes
3 2 1 -> no
'''
n = int(input('Введите ширину шоколадки в дольках:'))
m = int(input('Введите длинну шоколадки в дольках:'))
k = int(input('Введите колличество долек, которые хотите отломить:'))

if k % n == 0 or k % m == 0:
    print("от заданной шоколадки можно отломить желаемое колличество долек")
else:
    print("от заданной шоколадки нельзя отломить желаемое колличество долек")