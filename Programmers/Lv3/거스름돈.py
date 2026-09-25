# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12907


# DP 문제
def solution(n: int, money: list[int]) -> int:
    MOD = 1000000007
    # dp[i] = 지금까지 처리한 화폐들로 i원을 만드는 경우의 수
    dp = [0] * (n + 1)
    # 초기값. 화폐를 하나도 사용하지 않고 0원을 만드는 방법 1가지
    dp[0] = 1

    # 화폐 종류를 하나씩 추가해서 계산
    # -> 종류를 고정하고 순회하므로 순열이 아닌 조합으로 계산됨
    for m in money:
        for i in range(m, n+1):
            # 기존 방법(dp[i])는 그대로 두고,
            # i-m원을 만드는 방법에 m원을 하나 추가한 경우(dp[i-m])을 더함.
            dp[i] = (dp[i] + dp[i-m]) % MOD
    
    return dp[n]