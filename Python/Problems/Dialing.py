from sys import stdin

# Number 5622
def dialing(a):
    dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    time = 0
    for s in a:
        for i, d in enumerate(dial):
            if s in d:
                time += 3 + i
                break
    return time

alphabets = list(stdin.readline().strip())
print(dialing(alphabets))