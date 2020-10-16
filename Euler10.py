"""
Project Euler. Problem 10. 	Summation of primes
"""
import time


def is_prime(n):
    if n == 1: return False
    elif n < 4: return True
    elif n % 2 == 0: return False
    elif n < 9: return True
    elif n % 3 == 0: return False
    else:
        r = int(n**0.5)
        f = 5
        while f <= r:
            if n % f == 0: return False
            if n % (f + 2) == 0: return False
            f += 6
        return True


def gen_primes(n):
    '''
    Generate list of prime numbers not exceeding n.
    :param n: int : limit for primes what shall not be exceeded
    :return: list of primes
    '''
    primes = [2]
    a = 3
    for a in range(3, n + 1, 2):
        for i in primes:
            if i >= (a + 1)**0.5:
                primes.append(a)
                break
            if a % i == 0:
                break
    return primes

# This function should be used
def gen_primes_improved(n):
    '''
    Generate list of prime numbers not exceeding n.
    :param n: int : limit for primes what shall not be exceeded
    :return: list of primes
    '''
    primes = [2]
    # All even numbers initially marked as composite
    sive = [False, True] * (n // 2 + 1)
    # Check only odd value
    for d in range(3, n + 1, 2):
        if sive[d]:
            for ind in range(d * d, n + 1, d):
                sive[ind] = False
            primes.append(d)
    return primes


limit = 2000000


print("\nOptimized sieve of Erathosphenes algorithm from euler.net:")
star_time = time.time()
sivebound = (limit - 1) // 2
sive = [False] * (sivebound + 1)
crosslimit = int((limit**0.5 - 1) // 2)
for i in range(1, crosslimit + 1):
    if not sive[i]:
        for j in range(2 * i * (i + 1), sivebound + 1, 2 * i + 1):
            sive[j] = True
primes_sum = 2
for i in range(1, sivebound + 1):
    if not sive[i]: primes_sum += 2 * i + 1
print(primes_sum, sivebound)
print(f"Time: {time.time() - star_time} s.")


print("\nMy improved algorithm:")
star_time = time.time()
print(sum(gen_primes_improved(limit)))
print(f"Time: {time.time() - star_time} s.")


# Bad solutions, previous iterations
'''
print("\nMy algorithm:")
star_time = time.time()
print(sum(gen_primes(limit)))
print(f"Time: {time.time() - star_time} s.")
'''
'''
print("\nNatural looping algorithm:")
star_time = time.time()
primes_sum = 5
n = 5
while n <= limit:
    if is_prime(n): primes_sum += n
    n += 2
print(primes_sum)
print(f"Time: {time.time() - star_time} s.")
'''