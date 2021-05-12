from sys import stdin

# Number 2908
def sangsu(n):
    n = list(map(str, n.split()))
    x, y = int(n[0][::-1]), int(n[1][::-1])
    return x if x > y else y

numbers = stdin.readline().strip()
print(sangsu(numbers))