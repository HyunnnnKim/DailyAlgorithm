# Number 4344
def aboveAverage(num):
    count = 0
    avg = sum(num[1:]) / num[0]
    for i in num[1:]:
        if i > avg:
            count += 1
    pct = round((count / num[0]) * 100, 3)
    print('{0:.3f}%'.format(pct))

caseNum = int(input())
nums = list()
for i in range(caseNum):
    n = input()
    nums.append(list(map(int, n.split())))
    aboveAverage(nums[i])