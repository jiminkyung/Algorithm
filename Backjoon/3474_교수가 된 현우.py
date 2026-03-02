# 수학
# 정수론


# 문제: https://www.acmicpc.net/problem/3474
# 메모리: 32412KB / 시간: 160ms
from sys import stdin


input = stdin.readline

def main():
    T = int(input())

    for _ in range(T):
        N = int(input())

        num = 5
        cnt = 0

        # 5의 배수가 몇개씩 들어있는지 합산
        # 2 * 5 하나당 0이 하나씩 추가되는 셈인데, 2의 배수는 무수히 많으므로 5의 배수만 체크해주면 됨.
        while num <= N:
            cnt += N // num
            num *= 5
        
        print(cnt)


main()