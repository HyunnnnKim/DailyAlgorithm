from random import randint
import time

coins = [500, 100, 50, 10]
def ReturnNumberOfCoins(money):
    count = 0
    for coin in coins:
        count += money // coin
        money %= coin
    return count

def ReturnCoins(money):
    change = []
    for coin in coins:
        count = money // coin
        for _ in range(count):
            change.append(coin)
        money %= coin
    return change

cash = int(input('Input money for change: '))
startTime = time.time()

coinCount = ReturnNumberOfCoins(cash)
print('Number Of Coins: ', coinCount)

coins = ReturnCoins(cash)
print('Your Change: ', ' '.join(map(str, coins)))

endTime = time.time()
print('Elapsed Time: ', endTime - startTime)

