'''Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов 
(т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, 
если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, 
если с ритмом все не в порядке.

*Пример:*

**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
    **Вывод:** Парам пам-пам'''

'''a1 = input('Введите стихотворение: ')  .lower)'''

def Definition_of_vowels (list):
    n = 0
    for i in list:
        if i == 'а' or i == 'я' or i == 'у' or i == 'ю' or i == 'о' or i == 'е' or i == 'ё' or i == 'э' or i == 'и' or i == 'ы':
            n += 1
    return(n)


list_1 = (((input('Введите стихотворение: ')).lower()).split())
Number_of_vowels = []
list_2 = []
for i in range(len(list_1)):
    list_2 = list(list_1[i])
    n = Definition_of_vowels (list_2)
    Number_of_vowels.append(n)
    if Number_of_vowels[i] != Number_of_vowels[0]:
        print('Пам парам')
        break
    elif i == len(list_1)-1:
        print('Парам пам-пам')



