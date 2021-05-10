from sys import stdin

# Number 1978
def countPrime(c, nums):
    for n in nums:
        if n == 1: c -= 1
        for i in range(2, n):
            if n % i == 0:
                c -= 1
                break
    return c

count = int(input())
numbers = list(map(int, stdin.readline().strip().split()))
print(countPrime(count, numbers))