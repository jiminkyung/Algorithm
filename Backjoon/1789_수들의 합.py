# 수학
# 그리디 알고리즘


# 문제: https://www.acmicpc.net/problem/1789
# 메모리: 32412KB / 시간: 52ms

# x까지의 합이 S를 넘지 않을때까지 x를 증가시킴.
# ex) S = 200 일때, 1+2+...+19 = 190이므로 최대 x는 19다.
# => 1+2+...+18까지 더한다음 +29를 하면 200이 됨.
from sys import stdin


input = stdin.readline

def main():
    S = int(input())

    cnt = 0
    num = 1
    while S >= 0:
        S -= num
        num += 1
        cnt += 1

    print(cnt - 1)


main()