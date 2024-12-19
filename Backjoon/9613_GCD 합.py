# 문제집 - 0x12강 - 수학


# 문제: https://www.acmicpc.net/problem/9613
# 메모리: 32411KB / 시간: 288ms
from sys import stdin


input = stdin.readline

# 유클리드 호제를 이용한 gcd 함수
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


for _ in range(int(input())):
    line = list(map(int, input().split()))
    N = line[0]
    nums = line[1:]
    total_sum = 0

    for i in range(N):
        for j in range(i+1, N):
            total_sum += gcd(nums[i], nums[j])

    print(total_sum)