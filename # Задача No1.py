# Задача No1. Решение в группах
#За день машина проезжает n километров. 
#Сколько дней нужно, чтобы проехать маршрут
#длиной m километров? При решении этой задачи нельзя 
#пользоваться условной инструкцией if и циклами.
#Input:
#n = 700 m = 750 Output: 2


dis1 = int(input())
dis2 = int(input())
print((dis2 + dis1 - 1) // dis1)