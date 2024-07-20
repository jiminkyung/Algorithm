# 그리디 알고리즘
# 최대한 큰 값부터 체크한다.

# 메모리: 31120KB / 시간: 44ms

from sys import stdin


input = stdin.readline
N, K = map(int, input().split())
coins = [int(c) for c in stdin][::-1]

ret = 0

def greedy():
    global K, ret

    for c in coins:
        ret += K//c
        K %= c

    return ret

print(greedy())