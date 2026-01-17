# 구현
# 그리디 알고리즘
# 시뮬레이션


# 문제: https://www.acmicpc.net/problem/3205

# 주석이 달리면 다른 본문은 못 달리는 것으로 이해했지만 아님.
# 그냥 (본문-주석)이 잘리지 않고 한 페이지에 담겨있기만 하면 됨.

# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    N, K = map(int, input().split())
    F = int(input())
    lines = [1] * (N+1)

    for _ in range(F):
        X, Y = map(int, input().split())
        lines[X] += Y  # 본문에 주석 수 추가
    
    page = 1
    curr = 0

    for i in range(1, N+1):
        # 현재 페이지에 다 못 담는다면 새 페이지로
        if curr + lines[i] > K:
            page += 1
            curr = lines[i]
        else:
            curr += lines[i]
        
    print(page)


main()