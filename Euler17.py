"""
Project Euler. Problem 17. 	Number letter counts
"""

import time
import num2words

def get_writen(n):
    s1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
    s10 = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    sx0 = ['zero', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'hundred']
    h_suffix = 'hundred'

    th = (n % 1000000) // 1000
    h = (n % 1000) // 100
    t = (n % 100) // 10
    o = n % 10

    result = ''

    # Check thousands
    if th > 0:
        if th == 1:
            th_suffix = 'thousand'
        else:
            th_suffix = 'thousands'
        if result > '': result += ' '
        result += s1[th] + ' ' + th_suffix

    # Check hundreds
    if h > 0:
        if result > '': result += ' '
        result += s1[h] + ' ' + h_suffix

    # Check tens
    if t > 0:
        if result > '': result += ' and '
        if t > 1:
            result += sx0[t]
            # Check ones
            if o > 0:
                result += '-' + s1[o]
        else:
            t1 = n % 100
            result += s10[t1 - 10]
    else:
        if o > 0:
            if result > '': result += ' and '
            result += s1[o]

    return result, len(result.replace(' ', '').replace('-', ''))


checked_number = 1000

print('My function')
star_time = time.time()
print(checked_number)
letters_count = 0
for i in range(1, checked_number + 1):
    r = get_writen(i)
    letters_count += r[1]
print(letters_count)
print(f"Time: {time.time() - star_time} s.")

print('Using num2words')
star_time = time.time()
print(checked_number)
letters_count = 0
for i in range(1, checked_number + 1):
    letters_count += len(num2words.num2words(i).replace(' ', '').replace('-', ''))
print(letters_count)
print(f"Time: {time.time() - star_time} s.")

print(num2words.num2words(6532))
