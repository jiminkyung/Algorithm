# 동적 계획법 1

# 전깃줄은 순서대로 배치되어있음. 1 -> 9
# 전깃줄이 꼬이면 안됨. => 안꼬이려면 직전 전깃줄의 번호보다 커야함. => 오름차순
# "전체 전깃줄의 갯수 - 최대 증가 부분수열의 길이" 를 하면 될것같다.

# 메모리: 31120KB / 시간: 40ms
from sys import stdin


input = stdin.readline
N = int(input())
wires = sorted(tuple(map(int, input().split())) for _ in range(N))
numbers = list(zip(*wires))[1]

def checking_wires():
    dp = [1] * N

    for i in range(1, N):
        for j in range(i):
            if numbers[i] > numbers[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

    return max(dp)

print(N - checking_wires())


# 비슷하지만 실행시간이 32ms인 코드. 리스트 분리하는것보다 이게 더 깔끔한듯.
n = int(input())
lines = []
dp = [1] * n

for i in range(n):
    a, b = map(int, input().split())
    lines.append([a, b])

lines.sort()

for i in range(1, n):
    for j in range(0, i):
        if lines[j][1] < lines[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))