# 동적 계획법 1

# 메모리 초과
N = int(open(0).readline()) + 1

dp = [0] * (N+1)

dp[1] = dp[2] = 1

def fibonacci(n):
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

print(fibonacci(N) % 15746)


# 리스트를 미리 할당하지 않고 추가하는 방식으로 변경 => 메모리 초과
N = int(open(0).readline()) + 1

dp = [0, 1, 1]

def fibonacci(n):
    for _ in range(3, n+1):
        dp.append(dp[-1] + dp[-2])
    return dp[n]

print(fibonacci(N) % 15746)


# 리스트 사용 X => 통과.
# 메모리: 31120KB / 시간: 128ms

N = int(open(0).readline())

def fibonacci(n):
    a = b = 1
    for _ in range(3, n+1):
        a, b = b, (a+b) % 15746
    return b

print(fibonacci(N+1))