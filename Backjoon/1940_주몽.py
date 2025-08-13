# 정렬
# 두 포인터


# 문제: https://www.acmicpc.net/problem/1940
# 메모리: 33432KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    M = int(input())
    lst = sorted(map(int, input().split()))

    left, right = 0, N-1
    ret = 0

    while left < right:
        s = lst[left] + lst[right]

        # 기준보다 작으면 증가, 크면 감소시킴.
        if s < M:
            left += 1
        elif s > M:
            right -= 1
        # 기준을 만족하면 왼쪽, 오른쪽 모두 한칸씩 이동.
        else:
            left += 1
            right -= 1
            ret += 1
    
    print(ret)


main()