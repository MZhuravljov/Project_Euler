import time


def check_from_2palinfrome():
    '''
    Решение задачи поиска палиндрома, являющегося произведением двух двузначных чисел.
    выполняется перебор палиндромов, начиная с большего. Каждый проверяется на то, что делится нацело.
    '''
    star_time = time.time()
    for a in range(9, 0, -1):
        for b in range(9, -1, -1):
            current_value = int(''.join((str(a), str(b), str(b), str(a))))
            print(current_value)
            for i in range(99, int(current_value ** 0.5) - 1, -1):
                check_value = current_value // i
                if check_value < 100:
                    print(f" {i} * {check_value} = {i * check_value}")
                if current_value % i == 0 and current_value // i < 100:
                    print(f"{current_value} = {i} * {current_value // i}")
                    print(time.time() - star_time)
                    return


def check_from_3palinfrome():
    '''
    Решение задачи поиска палиндрома, являющегося произведением двух трёхзначных чисел.
    выполняется перебор палиндромов, начиная с большего. Каждый проверяется на то, что делится нацело.
    '''
    star_time = time.time()
    count_of_iteration = 0
    for a in range(9, 0, -1):
        for b in range(9, -1, -1):
            for c in range(9, -1, -1):
                #current_value = int(''.join((str(a), str(b), str(c), str(c), str(b), str(a))))
                current_value_digits = [a] + [b] + [c] + [c] + [b] + [a]
                current_value = int(''.join(str(i) for i in current_value_digits))
                for i in range(999, int(current_value ** 0.5) - 1, -1):
                    count_of_iteration += 1
                    if current_value % i == 0 and current_value // i < 1000:
                        print(f"{current_value} = {i} * {current_value // i}")
                        print(f"Time: {time.time() - star_time} s. Iterations: {count_of_iteration}")
                        return


def check_eulernet():
    '''
    Тест решения с euler.net перебором множителей
    '''
    star_time = time.time()
    count_of_iteration = 0
    END = 999
    big = 0
    for i in range(END, 100, -1):
        for j in range(END, i, -1):
            count_of_iteration += 1
            num = i * j
            if str(num) == str(num)[::-1]:
                if big < num: big = num
    print(big)
    print(f"Time: {time.time() - star_time} s. Iterations: {count_of_iteration}")

check_from_3palinfrome()
print("=============================================")
check_eulernet()

