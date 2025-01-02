# 문제집 - 0x14강 - 투 포인터


# 문제: https://www.acmicpc.net/problem/2230

# 도움이 됐던 반례👉 https://www.acmicpc.net/board/view/84249
# 메모리: 36264KB / 시간: 148ms
from sys import stdin


input = stdin.readline

N, M = map(int, input().split())
A = sorted(int(input()) for _ in range(N))

left, right = 0, 1
min_diff = float("inf")

while left <= right and right < N:
    diff = A[right] - A[left]

    # 만약 차이값이 M이라면 최적해이므로 바로 반환
    if diff == M:
        min_diff = M
        break

    if diff < M:
        right += 1
    else:  # diff > M 이라면 결과값 비교 후 업데이트
        min_diff = min(diff, min_diff)
        left += 1

print(min_diff)