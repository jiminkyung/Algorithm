# 조합론

# 공식을 이용한 단순 풀이.
# 메모리: 31120KB / 시간: 36ms
N, K = map(int, input().split())

ret = 1

for i in range(K):
    ret *= (N - i)

for i in range(1, K+1):
    ret //= i

print(ret)


# 파스칼의 삼각형 원리를 이용한 DP 풀이법.
# 큰 수가 주어질수록 효율이 좋다.
# 메모리: 31120KB / 시간: 40ms
def dynamic_programming(n, k):
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
    
    for i in range(n+1):
        for j in range(k+1):
            if j == 0 or j == i:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    
    return dp[n][k]

N, K = map(int, input().split())
print(dynamic_programming(N, K))