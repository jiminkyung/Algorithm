# 31120KB / 64ms
# 리암갤러거의 알바생활을 위한 문제

n = int(input())
coins = [25, 10, 5, 1]

changes = []

for _ in range(n):
    money = int(input())
    tmp = []
    for coin in coins:
        tmp.append(money//coin)
        money %= coin
    changes.append(tmp)

for row in changes:
    print(*row)