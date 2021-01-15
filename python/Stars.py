# Number 2438
def stars1(num):
    # for i in range(num):
    #     print('*', end='')
    #     for _ in range(i):
    #         print('*', end='')
    #     print()
    for i in range(1, (num + 1)):
        print('*' * i)

# Number 2439
def stars2(num):
    # for i in range(num):
    #     for _ in range(num - i , 1, -1):
    #         print(' ', end='')
    #     for _ in range(i + 1):
    #         print('*', end='')
    #     print()
    for i in range(1, (num + 1)):
        print(' ' * (num - i) + '*' * i)

# Number 2440
def stars3(num):
    # for i in range(num):
    #     for _ in range(i, num):
    #         print('*', end='')
    #     print()
    for i in range(num):
        print('*' * (num - i))

# Number 2441
def stars4(num):
    # for i in range(num):
    #     for _ in range(num - i, num):
    #         print(' ', end='')
    #     for _ in range(num - i, 0, -1):
    #         print('*', end='')
    #     print()
    for i in range(num):
        print(' ' * i + '*' * (n - i))

# Number 2442
def stars5(num):
    # for i in range(num):
    #     for _ in range(i, num - 1):
    #         print(' ', end='')
    #     for _ in range(0, (i * 2) + 1):
    #         print('*', end='')
    #     print()
    for i in range(num):
        print(' ' * (num - i - 1) + '*' * (i * 2 + 1))

n = int(input())
stars1(n)
stars2(n)
stars3(n)
stars4(n)
stars5(n)