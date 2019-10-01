import math
n = input("Enter a number: ")
n = int(n)
nums = []
primes = []
for num in range(0, n):
    nums.append(True)

sqroot = math.ceil(math.sqrt(len(nums)))
p = 2
while p < sqroot:
    j = p * p
    if nums[p - 1] == True:
        while j < len(nums):
            nums[j - 1] = False
            j += p 
    p += 1

for idx,num in enumerate(nums):
    if num == True:
        primes.append(idx + 1)
print(primes)

