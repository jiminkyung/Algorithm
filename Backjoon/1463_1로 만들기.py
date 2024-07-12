# 동적 계획법 1

# 메모리: 38932KB / 시간: 324ms
# 처음엔 dp = [0, 0, 1, 1] + [0]*(N-3), for문의 범위를 (4, N+1)로 작성함.
# N의 범위는 최소 1부터이므로 for문을 2부터 순회해야한다. (0, 1은 값이 0임)

N = int(input())

def make_one():
    dp = [0] * (N+1)

    for i in range(2, N+1):
        dp[i] = dp[i-1] + 1

        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)
        
    return dp[-1]

print(make_one())


# 실행시간 32ms인 코드. 메모이제이션, 1을 빼는 연산 제거, top-down 방식.
N = int(input())
cache = {1: 0}


def make_one(number):
    if 1 < number < 4:
        return 1

    if number in cache.keys():
        return cache[number]

    a_third = make_one(number // 3) + 1 + number % 3
    a_second = make_one(number // 2) + 1 + number % 2
    cache[number] = min(a_third, a_second)
    
    return cache[number]


print(make_one(N))