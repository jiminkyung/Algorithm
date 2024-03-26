# 못풀었다.
def solution(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    if n > 1:
        dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
    
    return dp[n]

# 피보나치 수열을 이용한다고 함.
# 아래는 리스트를 이용하지 않은 풀이다. 구관이 명관이다.
def solution(n):
    a, b = 1, 1
    for i in range(1, n):
        a, b = b, (a + b) % 1000000007
    return b