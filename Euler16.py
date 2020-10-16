"""
Project Euler. Problem 16. 		Power digit sum
"""

import time

star_time = time.time()
print(sum([int(i) for i in str(2**1000)]))
print(f"Time: {time.time() - star_time} s.")
