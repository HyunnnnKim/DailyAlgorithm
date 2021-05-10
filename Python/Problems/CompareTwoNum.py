# Number 1330
def compareTwoNum(nums):
    print('>') if nums[0] > nums[1] else print('<') if nums[0] < nums[1] else print('==')

numbers = input()
compareTwoNum(list(map(int, numbers.split())))