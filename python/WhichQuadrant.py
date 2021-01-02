# Number 14681
def whichQuadrant():
    if pointX > 0:
        print(1) if pointY > 0 else print(4)
    elif pointX < 0:
        print(2) if pointY > 0 else print(3)

pointX = float(input())
pointY = float(input())
whichQuadrant()