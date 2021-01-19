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

i = int(input())
print(groupWordChecker(i))