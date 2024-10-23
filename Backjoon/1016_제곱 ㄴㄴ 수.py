# 문제집 - BOJ 길라잡이 베타 (1)


# 문제: https://www.acmicpc.net/problem/1016

# 메모리 초과. 최대 입력값이 1,000,001,000,000 이다.
# 참고👉 https://www.acmicpc.net/board/view/148699 해서 수정한 코드.
# 메모리: 38932KB / 시간: 716ms

# 참고한 코드 그대로 for문 범위를 2, 1000000로 잡으면 700ms가 나온다.
# 많은양의 TC를 돌릴땐 무식하게 설정하는게 나은듯...
from sys import stdin


n, m = map(int, stdin.readline().split())

nums = [1] * (m - n + 1)

for i in range(2, int(m**0.5) + 1):
    s = i * i
    first = (n-1) // s + 1  # n 이상의 수 중 s로 나눠지는 가장 첫번째 수
    last = m // s  # m 이하의 수 중 s로 나눠지는 가장 마지막 수
    # ex) n = 10, s = 4 일때 first = 3 (3 * 4 = 12)

    for j in range(first, last+1):
        nums[j*s - n] = 0

print(sum(nums))