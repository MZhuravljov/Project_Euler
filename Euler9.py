"""
Project Euler. Problem 9. 	Special Pythagorean triplet
"""
import math
import time


def find_triplet(n):
    for a in range(1, n):
        b = n * (n-2 * a) // (2 * (n - a))
        c = int((a * a + b * b)**0.5)
        if a * a + b * b == c * c:
            return a, b, c


n = 1000
star_time = time.time()
triplet = find_triplet(n)
print(triplet)
print(math.prod(triplet))
print(f"Time: {time.time() - star_time} s.")
