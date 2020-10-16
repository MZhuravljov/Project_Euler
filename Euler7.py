"""
Project Euler. Problem 7. 	10001st prime
"""
import time


def gen_primes(n):
    '''
    Generate list of prime numbers not exceeding n.
    :param n: int : limit for primes what shall not be exceeded
    :return: list of primes
    '''
    primes = [2]
    a = 3
    for a in range(3, n):
        for i in primes:
            if i >= (a + 1)**0.5:
                primes.append(a)
                break
            if a % i == 0:
                break
        a += 1
    return primes


def gen_primes_no(num_of_primes):
    '''
    Generate list of prime numbers containing num_of_primes members.
    :param num_of_primes: int : number of primes what shall be generated
    :return: list of primes
    '''
    primes = [2]
    a = 3
    while len(primes) < num_of_primes:
        for i in primes:
            if i >= (a + 1)**0.5:
                primes.append(a)
                break
            if a % i == 0:
                break
        a += 1
    return primes

star_time = time.time()
primes = gen_primes_no(10001)
print(primes[-1])
print(f"Time: {time.time() - star_time} s.")
