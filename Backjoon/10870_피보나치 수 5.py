# 재귀

# 메모이제이션 사용해보기.
# 메모리: 31120KB / 시간: 32ms
def fibonacci(n):
    memo = {0: 0, 1: 1}

    def memoization(n):
        if n not in memo:
            memo[n] = memoization(n-1) + memoization(n-2)
        return memo[n]
    
    return memoization(n)

print(fibonacci(int(input())))