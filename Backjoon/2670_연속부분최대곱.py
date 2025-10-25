# 다이나믹 프로그래밍
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/2670

# 무식하게 풀어도 통과가 되긴 함. 하지만 DP를 사용하는게 훨씬 깔끔하다.

# 1) 단순 계산 풀이
# 메모리: 33432KB / 시간: 2428ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    lst = [float(input()) for _ in range(N)]
    # dp[i]: lst[i]부터 lst[N-1]까지의 곱 중 최댓값
    dp = [lst[i] for i in range(N)]

    for i in range(N):
        max_num = lst[i]
        num = lst[i]
        for j in range(i+1, N):
            num *= lst[j]
            if num > max_num:
                max_num = num
        dp[i] = max_num
    
    ret = max(dp)
    print(f"{ret:.3f}")  # 소수점 셋째자리까지 출력


main()


# 2) DP 사용 풀이
# 메모리: 33432KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    lst = [float(input()) for _ in range(N)]
    dp = [lst[i] for i in range(N)]

    for i in range(1, N):
        if dp[i-1] * dp[i] > dp[i]:
            dp[i] *= dp[i-1]
    
    print(f"{max(dp):.3f}")


main()