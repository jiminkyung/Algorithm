# 문제집 - 0x15강 - 해시


# 문제: https://www.acmicpc.net/problem/1351

# 재귀 + 메모이제이션 문제.
# 메모리: 32544KB / 시간: 40ms
from sys import stdin


input = stdin.readline

N, P, Q = map(int, input().split())

memo = {0: 1}  # A0 = 1

def dfs(num):
    # Anum이 memo에 존재한다면 해당 값 return
    if num in memo:
        return memo[num]

    ret = dfs(num // P) + dfs(num // Q)
    memo[num] = ret
    return ret

print(dfs(N))