# 1차원 배열


# 문제: https://www.acmicpc.net/problem/10811
# 메모리: 31252KB / 시간: 36ms
from sys import stdin


input = stdin.readline

N, M = map(int, input().split())
basket = list(range(N+1))

for _ in range(M):
    i, j = map(int, input().split())
    basket = basket[:i] + basket[i:j+1][::-1] + basket[j+1:]

print(*basket[1:])


# 다른 버전. 투 포인터 사용.
# 메모리/시간은 위 버전과 같다.
from sys import stdin


input = stdin.readline

N, M = map(int, input().split())
basket = list(range(N+1))

for _ in range(M):
    i, j = map(int, input().split())
    while i < j:
        basket[i], basket[j] = basket[j], basket[i]
        i += 1
        j -= 1

print(*basket[1:])