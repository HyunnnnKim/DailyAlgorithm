from sys import stdin

# Number 1406
def editor(txt, i):
    cursor = len(txt) - 1
    for _ in range(i):
        cmd = stdin.readline().strip()
        if cmd == 'L':
            if cursor == -1: continue
            cursor -= 1
        elif cmd == 'D':
            if cursor == len(txt) - 1: continue
            cursor += 1
        elif cmd == 'B':
            if cursor == -1: continue
            txt = txt[:cursor] + txt[cursor + 1:]
            cursor -= 1
        elif cmd[0] == 'P':
            txt = txt[:cursor + 1] + cmd[2:] + txt[cursor + 1:]
            cursor += 1
    return txt

def fasterEditor(txt, i):
    left = list(txt)
    right = list()
    for _ in range(i):
        cmd = stdin.readline().strip()
        if cmd == 'L':
            if left: right.append(left.pop())
        elif cmd == 'D':
            if right: left.append(right.pop())
        elif cmd == 'B':
            if left: left.pop()
        elif cmd[0] == 'P':
            left.append(cmd[2:])
    txt = ''.join(left + list(reversed(right)))
    return txt

text = stdin.readline().strip()
i = int(input())
print(editor(text, i))
print(fasterEditor(text, i))