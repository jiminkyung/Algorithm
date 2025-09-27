# 수학
# 정수론


# 문제: https://www.acmicpc.net/problem/2407
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    # 간단한 조합 문제다.
    # 조합 식은 nCr => n! / ((n-r)! r!) 인데, 이걸 계산하면 (n * n-1 * ... * n-r+1) / r! 이 된다. 
    n, m = map(int, input().split())

    top = bottom = 1

    # (n * n-1 * ... * n-r+1)
    for i in range(n, n-m, -1):
        top *= i
    
    # r!
    for i in range(1, m+1):
        bottom *= i
    
    print(top // bottom)


main()