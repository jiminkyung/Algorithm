# 문제집 - 0x14강 - 투 포인터


# 문제: https://www.acmicpc.net/problem/20366

# 좀 더 효율적인 방법이 있을거라 생각했는데 대부분 아래와 같이 풀었다.
# 메모리: 32412KB / 시간: 1428ms
from sys import stdin


input = stdin.readline

N = int(input())
snowball = sorted(map(int, input().split()))
min_diff = float("inf")

def two_pointer(left, right, target):
    global min_diff

    while left < right:
        ball = snowball[left] + snowball[right]
        diff = abs(target - ball)

        if diff == 0:  # 차이가 0이라면 프로그램 종료
            print(0)
            exit()

        min_diff = min(diff, min_diff)

        if ball < target:  # 기존 눈사람이 더 크다면 left 포인터 이동
            left += 1
        else:
            right -= 1


# 눈사람1은 조합으로 생성
for i in range(N):
    for j in range(i+3, N):
        # 눈사람1 범위 내에서 눈사람2 생성
        two_pointer(i+1, j-1, snowball[i] + snowball[j])

print(min_diff)