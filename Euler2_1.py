import time

# Ограничение для ряда Фибоначчи
fib_max_value = 4000000

startime = time.time()

# Перебираем два последних члена ряда и суммируем чётные
a = 1
b = 2
fib_sum = 0
while b < fib_max_value:
    if b % 2 == 0:
        fib_sum += b
    (a, b) = (b, a + b)

print(fib_sum)

print(time.time() - startime)