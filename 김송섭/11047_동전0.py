number_of_coin, target_price = map(int, input().split())
coins = []
for _ in range(number_of_coin):
    coins.append(int(input()))

result = 0
for i in range(len(coins) - 1, -1, -1):
    power = target_price // coins[i]
    if power > 0:
        target_price -= coins[i] * power
        result += power

print(result)