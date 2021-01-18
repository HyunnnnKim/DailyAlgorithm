from sys import stdin

# Number 1152
def wordCount(s):
    s = list(map(str, s.split()))
    return len(s)

sentence = stdin.readline().strip()
print(wordCount(sentence))