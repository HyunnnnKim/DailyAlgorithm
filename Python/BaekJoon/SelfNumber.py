# Number 4673
def selfNum(nums):
    result = set()
    for i in nums:
        for j in str(i):
            i += int(j)
        result.add(i)
    return sorted(nums - result)

numbers = set(range(1, 10001))
result = selfNum(numbers)
for n in result:
    print(n)