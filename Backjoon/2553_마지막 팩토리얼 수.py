# 수학
# 정수론


# 문제: https://www.acmicpc.net/problem/2553

# 참고👉 https://www.acmicpc.net/board/view/372
# 처음엔 % 10으로 일의 자리 숫자만 남겨놨었음. <- 틀림!
# 12 * 15 = 180이지만 2 * 15로 계산하면 30이 나와버림. 실제 마지막 숫자는 8이지만 3으로 인식해버리는것.

# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    MOD = 1000000  # 🚨 100000으로 설정 시 틀림
    # MOD1 = 1000000, MOD2 = 100000일때 결과값 차이는 여러번 발생함.
    # N = 9375일때 MOD1: 73668, MOD2: 8043 -> 이런식으로.

    num = 1

    for i in range(1, N+1):
        num *= i

        # 0 제거
        while num % 10 == 0:
            num //= 10
        
        num %= MOD

    print(num % 10)


main()