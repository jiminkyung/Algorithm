# 그리디 알고리즘


# 문제: https://www.acmicpc.net/problem/1049
# 메모리: 32544KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    N, M = map(int, input().split())

    pack = single = float("inf")

    for _ in range(M):
        p, s = map(int, input().split())
        pack = min(pack, p)  # 최소 패키지 값
        single = min(single, s)  # 최소 낱개 값
    
    # ⭐ 정답 후보는 세가지
    # 1. 정확하게 N개만큼 구입
    # - 패키지로 최대한 구매 후 남는 줄은 낱개로 구입
    # - 패키지보다 낱개 * 6 이 더 저렴할경우, 낱개로만 N개 구입
    # 2. N 이상 구입
    # - 패키지로만 구입
    # => 위 값 중 더 효율적인 값을 선택한다.
    if single * 6 < pack:
        total_cost = N * single
    else:
        pack_cost = (N // 6) * pack
        single_cost = (N % 6) * single

        total_cost = pack_cost + single_cost
        if N % 6 != 0:
            tmp = pack_cost + pack
            total_cost = min(total_cost, tmp)

    print(total_cost)


main()


# 💥 번외로, 만약 패키지 당 들어있는 줄의 갯수가 다르다면?
# DP로 풀어보고 싶었고 GPT에게 물어봄.

# N: 필요한 줄의 개수, M: 브랜드 수
N, M = map(int, input().split())
packages = []
singles = []

# 각 브랜드의 패키지 가격, 낱개 가격과 패키지 내 줄의 개수를 입력 받음
for _ in range(M):
    package_price, single_price, num_strings_in_package = map(int, input().split())
    packages.append((package_price, num_strings_in_package))
    singles.append(single_price)

# dp[i]는 i개의 줄을 구매하는 최소 비용
dp = [float('inf')] * (N + 1)
dp[0] = 0  # 0개의 줄은 0원으로 해결

# 동적 계획법으로 최소 비용을 계산
for i in range(1, N + 1):
    # 낱개로 하나씩 사는 경우
    dp[i] = min(dp[i], dp[i - 1] + min(singles))
    
    # 패키지를 사는 경우
    for package_price, num_strings_in_package in packages:
        if i >= num_strings_in_package:
            dp[i] = min(dp[i], dp[i - num_strings_in_package] + package_price)

# 결과는 dp[N]에 저장됨
print(dp[N])