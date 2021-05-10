# Number 10818
def findMinMax():
    n = int(input())
    nums = input()
    nums = list(map(int, nums.split()))
    print(str(min(nums)) + ' ' + str(max(nums)))

findMinMax()