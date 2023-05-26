"""Напишите программу, которая принимает на вход координаты
двух точек и находит
расстояние между ними в 2D пространстве"""
import math
from math import hypot
x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())

d = round(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), 2)
print(d)