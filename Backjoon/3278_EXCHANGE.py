# 다이나믹 프로그래밍


# 문제: https://www.acmicpc.net/problem/3278
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    mark = [0.0] * (N+1)
    dollar = [0.0] * (N+1)

    mark[0] = 100.0  # 처음엔 100 마르크 소유

    for i in range(1, N+1):
        B, S = map(int, input().split())

        # mark dollar 갱신 순서 바꿔도 상관 X
        # 전날 값 그대로 vs 전환
        mark[i] = max(mark[i-1], dollar[i-1] * (100 / S))
        dollar[i] = max(dollar[i-1], mark[i-1] * (B / 100))
    
    print(f"{mark[N]:.2f}")


main()