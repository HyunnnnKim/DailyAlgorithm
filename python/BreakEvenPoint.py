from sys import stdin

# Number 1712
def bep(nums):
    # 0: 고정 비용, 1: 가변 비용, 2: 매출액
    if nums[1] >= nums[2]: return -1
    return nums[0] // (nums[2] - nums[1]) + 1

value = stdin.readline().strip()
value = list(map(int, value.split()))
print(bep(value))
