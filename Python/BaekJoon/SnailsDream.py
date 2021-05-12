from sys import stdin
import math

def snailsDream(j):
    # 0: morning, 1: night, 2: tree
    days = j[2] / (j[0] - j[1])
    if days == int(days):
        days = math.ceil(days) - j[1]
    else:
        days = math.ceil(days)
    return days

def rightSol(j):
    days = (j[2] - j[1]) / (j[0] - j[1])
    return int(days) if days == int(days) else int(days) - 1

journey = list(map(int, stdin.readline().strip().split()))
print(snailsDream(journey))