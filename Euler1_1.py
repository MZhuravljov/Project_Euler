import time

range_limit = 1000

start_time = time.time()
print(sum([x for x in range(range_limit) if x%3 == 0 or x%5 == 0]))

print(time.time() - start_time)