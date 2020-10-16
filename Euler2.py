import time

# Ограничение для ряда Фибоначчи
fib_max_value = 4000000

startime = time.time()

# Генерируем ряд Фибоначчи
fib = [1, 2]
(*rest, fib_prelast,fib_last) = fib
while fib_prelast + fib_last < fib_max_value:
    fib += [fib_prelast + fib_last]
    (*rest, fib_prelast, fib_last) = fib
# Суммируем чётные члены
print(sum(x for x in fib if x%2 == 0))

print(time.time() - startime)