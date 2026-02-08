# 그리디 알고리즘


# 문제: https://www.acmicpc.net/problem/3279

# 3278_DOLLARS 문제와 거의 같음. DP 문제로 봐도 될 것 같다.
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    rates = [int(input()) for _ in range(N)]
    
    dollar = [0.0] * (N+1)
    mark = [0.0] * (N+1)
    
    # 처음엔 100딸라 소유
    dollar[0] = 100.0
    
    for i in range(1, N+1):
        rate = rates[i-1]
        
        # i일차에 달러를 보유하는 경우
        # 1. i-1일차에 달러였고 그대로 유지
        # 2. i-1일차에 마르크였고 달러로 환전
        dollar[i] = max(dollar[i-1], mark[i-1] * 100 / rate)
        
        # i일차에 마르크를 보유하는 경우
        # 1. i-1일차에 마르크였고 그대로 유지
        # 2. i-1일차에 달러였고 마르크로 환전
        mark[i] = max(mark[i-1], dollar[i-1] * rate / 100)
    
    # 마지막은 반드시 달러로
    print(f"{dollar[N]:.2f}")


main()