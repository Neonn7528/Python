"""Задача 10: На столе лежат n монеток. 
Некоторые из них лежат вверх решкой, а 
некоторые – гербом. Определите минимальное 
число монеток, которые нужно перевернуть, 
чтобы все монетки были повернуты вверх 
одной и той же стороной. Выведите минимальное 
количество монет, которые нужно перевернуть"""

"""import random
from random import randint
quantity = int(input('Введите количество монет: '))
a = 0
b = 0
coins = [0, 1]
for i in range(quantity):
     random.shuffle(coins)
     if int(coins[0]) == 0:
         a += 1
     if int(coins[0]) == 1:
         b += 1
print(f'Орёл-{a}, Решка-{b}.')

if a > b:
     min = b
else:
     min = a
print(f"Mинимальное количество монет, которые нужно перевернуть = {min}")"""


"""Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих 
чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа."""
"""
print('Введите сумму чисел и их произведение через пробел: ')
a, b = map(int, input().split())
status = True
for x in range(a + b):
    status = False
    for y in range(a + b):
        if x + y == a and x * y == b:
            print(f'Загаданные числа: {x} и {y}')
            status = False"""


"""Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N."""

n = int(input("Введите число: "))
m = 1
while m < n:
    print(m, end=' ')
    m = m * 2