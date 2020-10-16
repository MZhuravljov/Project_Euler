"""
Project Euler. Problem 15. 	Lattice paths
"""

import time
import math


def can_move(x, y):
    possible_move = [0, 0]
    if x < grid_size: possible_move[0] = 1
    if y < grid_size: possible_move[1] = 1
    return possible_move


def check_path(x, y):
    global paths_count
    possible_path = [0, 0]
    if x < grid_size: possible_path[0] = 1
    if y < grid_size: possible_path[1] = 1
    if possible_path == [0, 0]:
        paths_count += 1
        return 1
    if possible_path[0] == 1:
        check_path(x + 1, y)
    if possible_path[1] == 1:
        check_path(x, y + 1)


def get_route_count(x, y):
    a = [[0 for x in range(0, grid_size + 1)] for y in range(grid_size + 1)]
    a[0][0] = 1
    for crow in range(0, grid_size + 1):
        for ccol in range(0, grid_size + 1):
            if ccol < grid_size:
                a[crow][ccol + 1] += a[crow][ccol]
            if crow < grid_size:
                a[crow + 1][ccol] += a[crow][ccol]
    return a[grid_size][grid_size]

def get_route_combi(n):
    '''
    Вычисляет количество путей как количесво сочетаний 2*n (количество шагов в каждом пути)
    из
    :param n:
    :return:
    '''
#    r = math.factorial(2 * n) // math.factorial(n)**2
    r = math.factorial(2 * n * (n + 1)) // math.factorial(n) * math.factorial(2 * n * n)
    return r


grid_size = 2

'''paths_count = 0
star_time = time.time()
check_path(0, 0)
print(f"Recursion -> For grid {grid_size}x{grid_size} are possible {paths_count} routs.")
print(f"Time: {time.time() - star_time} s.")
'''
star_time = time.time()
routs_count = get_route_count(0, 0)
print(f"Array -> For grid {grid_size}x{grid_size} are possible {routs_count} routs.")
print(f"Time: {time.time() - star_time} s.")

star_time = time.time()
routs_count = get_route_combi(grid_size)
print(f"Combinatorial -> For grid {grid_size}x{grid_size} are possible {routs_count} routs.")
print(f"Time: {time.time() - star_time} s.")
