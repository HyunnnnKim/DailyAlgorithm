# Number 1065
def constantNumStr(num):
    result = 99
    if num < 100:
        result = num
    else:
        for n in range(111, num + 1):
            sNum = str(n)
            if int(sNum[0]) - int(sNum[1]) == int(sNum[1]) - int(sNum[2]):
                result += 1
    return result

def constantNum(num):
    result = 99
    if num < 100:
        result = num
    else:
        for n in range(111, num + 1):
            hundreds = n // 100
            tens = (n % 100) // 10
            ones = (n % 100) % 10
            if hundreds - tens == tens - ones:
                result += 1
    return result

num = int(input())
print(constantNumStr(num))
print(constantNum(num))