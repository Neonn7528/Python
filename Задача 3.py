"""Задача №3. Решение в группах
В некоторой школе решили набрать три новых
математических класса и оборудовать кабинеты для
них новыми партами. За каждой партой может сидеть
два учащихся. Известно количество учащихся в
каждом из трех классов. Выведите наименьшее
число парт, которое нужно приобрести для них.
Input: 20 21 22(ввод чисел НЕ в одну строку)
Output: 32"""

cl1 = int(input())
cl2 = int(input())
cl3 = int(input())

num1 = (cl1 + maxDesk - 1) // maxDesk
num2 = (cl2 + maxDesk - 1) // maxDesk
num3 = (cl3 + maxDesk - 1) // maxDesk

res = num1 + num2 + num3
print(res)