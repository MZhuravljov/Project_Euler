"""
Project Euler. Problem 14. 	Longest Collatz sequence
"""

import time


def get_sequence(n):
    sequence = [n]
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence


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
star_time = time.time()
max_len = 1
max_len_s = 1
current_len = 0
s = start_num_limit // 2 + 1
while s < start_num_limit:
    current_len = get_sequence_len(s)
    if current_len > max_len:
        max_len = current_len
        max_len_s = s
    s += 1
print(s)
print(f"Start number {max_len_s} produces sequence {max_len} numbers length.")
print(f"Time: {time.time() - star_time} s.")
