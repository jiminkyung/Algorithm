# 수학
# 조합론


# 문제: https://www.acmicpc.net/problem/3049
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    # 교차점 하나를 만드려면 두 개의 대각선이 필요.
    # => 4개의 꼭짓점이 필요함. 즉, N개의 꼭짓점 중 4개를 선택하는 경우를 구하면 됨.
    N = int(input())

    ret = 1

    for i in range(N-3, N+1):
        ret *= i
    
    print(ret // 24)


main()