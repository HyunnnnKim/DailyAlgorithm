from sys import stdin
import sys

# Number 10757
def bigNum(n):
    print(type(n[0] + n[1]))
    print(sys.getsizeof(type(n[0] + n[1])))
    return n[0] + n[1]

nums = list(map(int, stdin.readline().strip().split()))
print(bigNum(nums))
