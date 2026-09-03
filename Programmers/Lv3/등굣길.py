# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42898


def solution(m, n, puddles: list[list[int]]) -> int:
    MOD = 1000000007
    dp = [[0] * (m + 1) for _ in range(n + 1)]  # 0행, 0열에 패딩처리. 1-based.
    dp[1][1] = 1  # 시작값

    # 🚨 웅덩이 좌표가 (열, 행) 순으로 주어지므로 주의해야함
    puddles = {(j, i) for i, j in puddles}

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (i, j) in puddles:  # 물 웅덩이일경우 건너뜀
                continue

            # 현 위치의 위, 왼쪽 좌표의 경우의 수를 더해줌
            dp[i][j] += (dp[i-1][j] + dp[i][j-1]) % MOD
    
    return dp[n][m]