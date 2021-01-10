# Number 10809
def findAlphabet(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = [-1] * len(alphabet)
    for i, c in enumerate(s):
        j = alphabet.find(c)
        if result[j] == -1:
            result[j] = i
    return result

s = input()
print(" ".join(str(x) for x in findAlphabet(s)))