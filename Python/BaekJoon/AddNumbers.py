# Number 11720
def addNumbers(nums):
    result = 0
    for x in nums:
        result += int(x)
    return result

n = int(input())
numbers = input()
print(addNumbers(numbers))