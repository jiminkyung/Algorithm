# 기하2


# 문제: https://www.acmicpc.net/problem/2166

# 벡터의 외적, 슈오카 공식을 사용하여 풀어야 함.
# 참고👉 https://darkpgmr.tistory.com/86

# 메모리: 32140KB / 시간: 44ms
from sys import stdin


input = stdin.readline

N = int(input())
coordinate = [tuple(map(int, input().split())) for _ in range(N)]

coordinate.append(coordinate[0])

ret = 0
for i in range(N):
    ret += coordinate[i][0] * coordinate[i+1][1] - coordinate[i+1][0] * coordinate[i][1]

print(abs(ret) / 2)