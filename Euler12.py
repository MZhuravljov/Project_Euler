"""
Project Euler. Problem 12. 	Highly divisible triangular number
"""
import math
import time


def factor(n):
    '''
    Раскладывает чсило n на простыет множители и подсчитывает количество делителей числа.
    :param n:
    :return: кортеж из трёх значений:
            - список простых множителей числа n
            - список количества каждого множителя в разложении
            (степень s1, s2, .... sn каждого простого множителя в разложении a = p^s1 * p^s2 * p^s3 * .... * p^sn)
            - общее количество делителей числа (s1 + 1) * (s2 + 1) * (s3 + 1) * ... * (sn + 1)
            см. https://zaochnik.com/spravochnik/matematika/delimost/nahozhdenie-vseh-delitelej-chisla/
    '''
    result = []
    factors_count = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            if len(result) == 0 or result[-1] != d:
                factors_count.append(1)
            else:
                factors_count[-1] += 1
            result.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        if len(result) == 0 or result[-1] != n:
            factors_count.append(1)
        else:
            factors_count[-1] += 1
        result.append(n)
    count_of_factors = math.prod([i + 1 for i in factors_count])
    return result, factors_count, count_of_factors


divisors_count_value = 500

star_time = time.time()
number = 1
item = 1
triangle = 1
while number <= divisors_count_value:
    item += 1
    print(item, end='\r')
    triangle += item
    factorization = factor(triangle)
    number = factorization[2]
print(triangle, " -> ", number, " -> ", factorization[0], " -> ", factorization[1])
print(f"Time: {time.time() - star_time} s.")
