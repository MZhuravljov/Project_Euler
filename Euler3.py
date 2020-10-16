"""
Project Euler. Problem 3. 	Largest prime factor
"""
import time


def isPrime(n):
    '''
    Проверяет, является ли число простым
    :param n: проверяемое число
    :return: true если число является простым
    '''
    if n % 2 == 0:
        return n == 2
    d = 3
    while (n % d) != 0 and (d * d <= n):
        d += 2
    return d * d > n


key_value = 600851475143
start_time = time.time()
dividers = (x for x in range(int(key_value ** 0.5), 1, -1) if key_value % x == 0 and isPrime(x))
print(max(dividers))
print(time.time() - start_time)
