from sys import stdin

# Number 1316
def groupWordChecker(i):
    count = i
    for _ in range(i):
        word = list(stdin.readline().strip())
        done = list(word.pop())
        for w in reversed(word):
            if w != done[-1] and w in done:
                count -= 1
                break
            done.append(word.pop())
    return count

def betterSol(i):
    result = 0
    for _ in range(i):
        word = stdin.readline().strip()
        if list(word) == sorted(word, key = word.find):
            result += 1
    return result

i = int(input())
print(groupWordChecker(i))
print(betterSol(i))