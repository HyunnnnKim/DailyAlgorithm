from sys import stdin

# Number 1157
def mostUsedLetter(w):
    cap = list(w.upper())
    noDup = list(set(cap))
    count = list((0,))
    result = ''
    for d in noDup:
        c = cap.count(d)
        if count[0] < c:
            count.clear()
            count.append(c)
            result = d
        elif (count[0] == c):
            count.append(c)
    if len(count) > 1: result = '?'
    return result

def betterSol(w):
    cap = w.upper()
    cap_u = list(set(cap))
    cnt_list = []
    result = '?'
    for x in cap_u:
        cnt = cap.count(x)
        cnt_list.append(cnt)
    if cnt_list.count(max(cnt_list)) == 1:
        max_index = cnt_list.index(max(cnt_list))
        result = cap_u[max_index]
    return result

word = stdin.readline().strip()
print(mostUsedLetter(word))
print(betterSol(word))