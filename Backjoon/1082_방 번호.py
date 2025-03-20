# 다이나믹 프로그래밍


# 문제: https://www.acmicpc.net/problem/1082

# DFS 방식으로 풀어보다가 결국 풀이를 찾아본 문제... 1차원 DP로 해결 가능함.
# 출처👉 https://jun-bae.tistory.com/42
# DP 연습을 열심히 하자. 나중에 다시 풀어봐야할 문제.

# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    P = list(map(int, input().split()))
    M = int(input())

    dp = [-1] * (M+1)  # dp[x]: x원으로 살 수 있는 최대 방 번호

    for i in range(N-1, -1, -1):  # 큰 번호부터 체크
        cost = P[i]
        for j in range(cost, M+1):  # i번의 가격부터 M원까지 체크
            # dp[j-cost]*10 + i: 기존 방 번호 뒤에 현재 번호 i를 붙인 값
            # j원으로 살 수 있는 방 번호 갱신
            # => (기존 방 번호, 현재 번호 i, 기존 방 번호에 i를 붙인 값) 중 큰 값으로 설정
            dp[j] = max(dp[j], i, dp[j-cost]*10 + i)
    
    print(dp[M])


main()