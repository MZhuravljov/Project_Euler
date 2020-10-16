"""
Project Euler. Problem 6. 	Sum square difference
"""
count_of_numbers = 100
print(sum(x for x in range(1, count_of_numbers + 1))**2 - sum(x*x for x in range(1, count_of_numbers + 1)))
