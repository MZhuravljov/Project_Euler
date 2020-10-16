import time

range_limit = 1000

start_time = time.time()
s = 0
for i in range(1, range_limit):
    if i % 3 == 0 or i % 5 == 0:
        s += i
print(time.time() - start_time)

print(f"The sum of all the multiples of 3 or 5 below {range_limit} is {s}")
