# Number 10952
def aPlusB5():
    while True:
        num = input()
        n = list(map(int, num.split()))
        if n[0] == 0 and n[-1] == 0: break
        print(n[0] + n[-1])

aPlusB5()