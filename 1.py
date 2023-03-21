'''На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, 
чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть'''

from random import randint # не разобрался зачем это

n = int(input('введите кол-во монет:\n>>> '))
coin_arrangement = [randint(0, 1) for _ in range(n)]
print(coin_arrangement)
front_side = 0
flip_side = 0
for side in coin_arrangement:
    if side == 0:
        front_side += 1
    else:
        flip_side += 1
if front_side <= flip_side:
    print ('нужно перевернуть', front_side, 'монет')
else:
    print ('нужно перевернуть', flip_side, 'монет')        