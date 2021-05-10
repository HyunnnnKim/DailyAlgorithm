# Number 15596
def sumOfN(nums):
    result = 0
    for x in nums:
        result += x
    return result

numbers = input()
numbers = list(map(int, numbers.split()))
print(sumOfN(numbers))