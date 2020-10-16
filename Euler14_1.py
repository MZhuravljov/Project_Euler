"""
Project Euler. Problem 14. 	Longest Collatz sequence
"""

import time



values = {1: 1}


def Collatz(n):
    if n == 1: return [1]
    if n % 2 == 0:
        return [n] + Collatz(n // 2)
    else:
        return [n] + Collatz(3 * n + 1)

def get_sequence_len(n):
    l = 1
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        l += 1
    return l




start_num_limit = 1000000

lengths = [0] * (start_num_limit + 1)
star_time = time.time()
max_len, max_i = 0, 0
#lengths[start_num_limit // 2] = len(Collatz(start_num_limit // 2))
for i in range(start_num_limit, start_num_limit // 2 + 1, -1):
    if i % 2 == 0 and lengths[i // 2] != 0:
        lengths[i] = 1 + lengths[i // 2]
    elif lengths[(3 * i + 1) // 2] != 0:
        lengths[i] = 2 + lengths[(3 * i + 1) // 2]
    else:
        lengths[i] = get_sequence_len(i)
    if lengths[i] > max_len:
        max_len = lengths[i]
        max_i = i

#print(Collatz(start_num_limit))

print(f"Start number {max_i} produces sequence {max_len} numbers length.")
print(f"Time: {time.time() - star_time} s.")


