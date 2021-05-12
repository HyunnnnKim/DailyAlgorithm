from sys import stdin

# Number 2675
def repeatString(i):
    for _ in range(i):
        result = ''
        line = stdin.readline().strip()
        for s in line[2:]:
            result += s * int(line[0])
        print(result)

i = int(input())
repeatString(i)