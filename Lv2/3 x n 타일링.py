# gpt 풀이.
def solution(n):
    if n % 2 != 0:  # 홀수인 경우 채울 수 없음
        return 0
    
    dp = [0] * (n+1)  # dp 테이블 초기화
    dp[0], dp[2] = 1, 3  # 초기 조건 설정
    
    for i in range(4, n+1, 2):  # 4부터 시작하여 짝수만 고려
        dp[i] = dp[i-2] * 3 + sum(dp[:i-2]) * 2  # 점화식 적용
        dp[i] %= 1_000_000_007  # 문제 조건에 따른 나머지 연산
    
    return dp[n]