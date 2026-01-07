# 수학
# 그리디 알고리즘


# 문제: https://www.acmicpc.net/problem/3135
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    A, B = map(int, input().split())
    N = int(input())
    channel = [int(input()) for _ in range(N)]
    # 목표 채널과 가까운 순으로 정렬
    channel.sort(key=lambda x: abs(B - x))

    # cnt_1: 단순 이동, cnt_2: 가까운 채널에서 이동
    cnt_1 = abs(B - A)
    cnt_2 = abs(channel[0] - B) + 1

    print(min(cnt_1, cnt_2))


main()