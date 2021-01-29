# Number 2581
def primeNum(a, b):
    total = []
    for n in range(a, b + 1):
        if n < 2: continue
        total.append(n)
        for i in range(2, n):
            if n % i == 0:
                total.pop()
                break;
    if len(total) > 0:
        print(sum(total))
        print(min(total))
    else: print(-1)

m = int(input())
n = int(input())
primeNum(m, n)