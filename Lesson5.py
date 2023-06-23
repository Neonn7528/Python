"""факториал числа найти. 
вводите число и находите рекурсией его факториал. 
для 5 факториал 120"""

"""n = int(input('Введите число: '))
factorial = 1
while n > 1:
    factorial *= n
    n -= 1
print(factorial)"""


"""Задача No31. Решение в группах
Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). Требуется найти N-е число Фибоначчи
Input: 7 Output: 21
Задание необходимо решать через рекурсию"""

def fibonacciGenerator():
    a=b=1
    while True:
        yield a
        a,b=b,a+b
fib=fibonacciGenerator()
for i in fib:
    if i>100:
        break
    else:
        print(i)
    