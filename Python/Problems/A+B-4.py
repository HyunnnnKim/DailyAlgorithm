import sys

# Number 10951
for n in sys.stdin:
    try:
        n = list(map(int, n.split()))
        print(n[0] + n[-1])
    except:
        break