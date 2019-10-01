import sys
import math
num = input("Enter a number: ")
num = int(num)


def is_prime(num):
    m = 2
    k = 1
    while m < 4:
        if num % m == 0:
            return False
        m += 1
    while 6 * k - 1 < math.sqrt(num):
        if num % (6 * k + 1) == 0 or num % (6 * k - 1) == 0:
            return False
        k += 1
    return True


print(is_prime(num))
