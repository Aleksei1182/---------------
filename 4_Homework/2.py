'''В фермерском хозяйстве в Карелии выращивают чернику. 
Она растет на круглой грядке, причем кусты высажены только по окружности. 
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора
на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, 
которое может собрать за один заход собирающий модуль, 
находясь перед некоторым кустом заданной во входном файле грядки.'''

from random import randint 

n = int(input('введите кол-во кустов на гряде>>> '))
NumberBerriesBushes = [randint(50, 100) for _ in range(n)]
print(NumberBerriesBushes)
NumberBerriesBushes.append(NumberBerriesBushes[0])
print(NumberBerriesBushes)

MaximumBerries = NumberBerriesBushes[0]
for i in range(len(NumberBerriesBushes)-2):
    if NumberBerriesBushes[i] + NumberBerriesBushes[i+1] + NumberBerriesBushes[i+2] > MaximumBerries:
        MaximumBerries = NumberBerriesBushes[i] + NumberBerriesBushes[i+1] + NumberBerriesBushes[i+2]
if len(NumberBerriesBushes) == 3:
    MaximumBerries = NumberBerriesBushes[0] + NumberBerriesBushes[1]
print(MaximumBerries)


