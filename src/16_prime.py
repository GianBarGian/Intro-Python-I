import sys
import math
num = input("Enter a number: ")
num = int(num)

start = 2

def is_prime(num):
    m = 2
    while m < math.sqrt(num):
        print(m)
        if num % m == 0:
            return False
        m += 1
    return True

print(is_prime(num))