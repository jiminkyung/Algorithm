# 누적 합

# 메모리: 40156KB / 시간: 100ms
from sys import stdin


input = stdin.readline
N, K = map(int, input().split())
temperature = list(map(int, input().split()))

curr = sum(temperature[:K])
max_temp = curr

for i in range(1, N-K+1):
    curr -= temperature[i-1]
    curr += temperature[i+K-1]
    max_temp = max(max_temp, curr)

print(max_temp)


# enumerate 사용
# 메모리: 40156KB / 시간: 96ms
from sys import stdin


input = stdin.readline
N, K = map(int, input().split())
temperature = list(map(int, input().split()))

curr = sum(temperature[:K])
# max_temp = float("-inf") => 첫 curr값이 최댓값일 경우를 고려하지 못함.
max_temp = curr

for i, temp in enumerate(temperature[K:]):
    curr -= temperature[i]
    curr += temp
    max_temp = max(max_temp, curr)

print(max_temp)