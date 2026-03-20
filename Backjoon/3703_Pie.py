# 기하학
# 이분 탐색
# 매개 변수 탐색


# 문제: https://www.acmicpc.net/problem/3703
# 메모리: 35560KB / 시간: 204ms
from sys import stdin
from math import pi


input = stdin.readline

def main():
    T = int(input())

    for _ in range(T):
        solve()


def solve():
    # N: 파이 수, F: 친구 수
    N, F = map(int, input().split())
    # 부피 = pi * r^2 * 높이 인데, 높이는 항상 1이니 pi * r^2.
    # 🗝️ 이분탐색으로 어느 부피만큼의 조각(mid)으로 나눌건지 결정한다.
    # 만약 mid로 각 파이를 나눠서 나온 총 조각 갯수가 F + 1개 이상이라면, 크기를 더 키워보는거임.
    radius = list(map(int, input().split()))
    volume = [pi * r ** 2 for r in radius]

    start, end = 0.0, max(volume)

    # 실수형 이분탐색은 for문으로 돌리는게 나음.
    for _ in range(100):
        mid = (start + end) / 2

        cnt = sum(int(vol / mid) for vol in volume)

        # mid만큼 나눠서 나온 조각 수가 F + 1(본인 포함)개일경우 start 갱신
        if cnt >= F + 1:
            start = mid
        else:
            end = mid
    
    print(f"{start:.4f}")


main()