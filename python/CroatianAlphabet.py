# Number 2941
def croatianAlphabet(alphabets):
    ca = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    count = 0
    i = 0
    while i < len(ca):
        if ca[i] not in alphabets:
            i += 1
        else:
            count += 1
            alphabets = alphabets.replace(ca[i], '3', 1)
    alphabets = list(filter(('3').__ne__, alphabets))
    count += len(alphabets)
    return count

def betterSolution(alphabets):
    ca = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    for a in ca:
        alphabets = alphabets.replace(a, '*')
    return len(alphabets)

letters = input()
print(croatianAlphabet(letters))
print(betterSolution(letters))