# Number 9498
def testResult(score):
    if score in range(90, 101): print('A')
    elif score in range(80, 90): print('B')
    elif score in range(70, 80): print('C')
    elif score in range(60, 70): print('D')
    else: print('F')

testResult(int(input()))