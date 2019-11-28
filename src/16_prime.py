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

def is_prime_improve(num):
    primes =  [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 200]
    for prime in primes:
        print(prime)
        if prime < num and num % prime == 0:
            return False
    return True

print(is_prime_improve(num))