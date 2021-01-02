# Number 1110
def addCycle():
    num = compareVal = int(input())
    count = 0
    while True:
        tens = int(num // 10)
        ones = int(num % 10)
        result = tens + ones
        count += 1

        if result >= 10:
            result = int(result % 10)
        num = (ones * 10) + result

        if num == compareVal:
            break
    return count

print(addCycle())