# Number 2438
def stars1(num):
    for i in range(num):
        print('*', end='')
        for j in range(i):
            print('*', end='')
        print()

# Number 2439
def stars2(num):
    for i in range(num):
        for _ in range(num - i , 1, -1):
            print(' ', end='')
        for _ in range(i + 1):
            print('*', end='')
        print()

stars1(int(input()))
stars2(int(input()))