# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/43105


# DP 문제
def solution(triangle: list[list[int]]) -> int:
    N = len(triangle)
    dp = [line[:] for line in triangle]

    # 끝에서부터 채워넣기
    # dp[i][j]: triangle[i][j] + max(왼쪽 아래 dp값, 오른쪽 아래 dp값)
    for i in range(N-2, -1, -1):
        for j in range(i+1):
            dp[i][j] = max(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]
    
    return dp[0][0]