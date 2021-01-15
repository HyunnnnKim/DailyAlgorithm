# Number 1546
def average(scores):
    m = max(scores)
    tot = 0
    for s in scores:
        tot += s / m * 100
    return tot / len(scores)

i = int(input())
x = input()
print(average(list(map(int, x.split()))))