# Number 8958
def oxQuiz(answer):
    a = list(answer)
    point = 0
    total = 0
    for x in a:
        if x == 'O':
            point += 1
            total += point
        else:
            point = 0
    return total

i = int(input())
for _ in range(i):
    a = input()
    print(oxQuiz(a))