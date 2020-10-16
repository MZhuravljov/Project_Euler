"""
Project Euler. Problem 5
"""
import math
import time

def lcm(a, b):
    '''
    Calculate Lower common multiple for two numbers
    :param a: int : First number
    :param b: int : Second number
    :return: int : LCM
    '''
    return abs(a * b) // math.gcd(a, b)


def lcm_list(alist):
    '''
    Calculate Lower common multiple for the list
    :param alist: list for calculation
    :return: int : LCM for list
    '''
    if len(alist) == 2:
        return abs(alist[1] * alist[0]) // math.gcd(alist[1], alist[0])
    else:
        return abs(alist[0] * lcm_list(alist[1:])) // math.gcd(alist[0], lcm_list(alist[1:]))


star_time = time.time()
A = [x for x in range(1, 21)]
print(lcm_list(A))
print(f"Time: {time.time() - star_time} s.")

