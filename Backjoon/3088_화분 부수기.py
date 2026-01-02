# 그리디 알고리즘


# 문제: https://www.acmicpc.net/problem/3088
# 메모리: 68252KB / 시간: 452ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())

    cnt = 1
    nums = set(map(int, input().split()))  # 제일 왼쪽 화분

    for _ in range(N-1):
        curr = set(map(int, input().split()))

        # 겹치는 게 하나도 없을 경우 추가로 깨야함.
        if not nums & curr:
            cnt += 1
        # 현재 화분 숫자 추가
        nums |= curr
    
    print(cnt)


main()