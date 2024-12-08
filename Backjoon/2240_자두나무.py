# 문제집 - 0x10강 - 다이나믹 프로그래밍


# 문제: https://www.acmicpc.net/problem/2240
# 참고👉 https://wooono.tistory.com/643

# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

T, W = map(int, input().split())
tree = [0] + [int(input()) for _ in range(T)]
dp = [[0] * (W+1) for _ in range(T+1)]

for i in range(1, T+1):  # 1초부터 T초까지
    for j in range(W+1):  # 0번부터 W번까지
        # 1. 한번도 움직이지 않은 상태일 경우
        if j == 0:
            if tree[i] == 1:
                dp[i][j] = dp[i-1][j] + 1
            else:
                dp[i][j] = dp[i-1][j]
        else:
            # 2. 자두가 1번 나무에서 떨어지고 현재 1번에 위치 or 2번 나무에서 떨어지고 현재 2번에 위치
            if (tree[i] == 1 and j % 2 == 0) or (tree[i] == 2 and j % 2 == 1):
                # (이전 위치에서 현재 위치로 이동했을경우, 이전위치 = 현재위치라서 같은 자리에 있을 경우)
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[T]))