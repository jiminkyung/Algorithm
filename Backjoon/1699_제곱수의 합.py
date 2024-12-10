# 문제집 - 0x10강 - 다이나믹 프로그래밍


# 문제: https://www.acmicpc.net/problem/1699
# 참고: https://velog.io/@fill0006/%EB%B0%B1%EC%A4%80-1699%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A0%9C%EA%B3%B1%EC%88%98%EC%9D%98-%ED%95%A9

# 메모리: 33192KB / 시간: 4428ms
N = int(input())

dp = [0] * 100001

for i in range(1, N+1):
    # 만약 i가 어떤 수의 제곱이라면 1로 설정
    if int(i ** 0.5) == i ** 0.5:
        dp[i] = 1
    else:
        min_value = int(1e9)
        # 1부터 i의 제곱근까지 반복
        # dp[i] = i - j**2 의 dp값 + 1
        # 1은 j**2를 더하는 경우를 의미함
        for j in range(1, int(i ** 0.5)+1):
            min_value = min(min_value, dp[i - j**2])
        dp[i] = min_value + 1

print(dp[N])