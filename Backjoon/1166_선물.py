# 이분 탐색


# 문제: https://www.acmicpc.net/problem/1166

# ⭐ 실수형 이분탐색 문제. 정수형처럼 설계 시 무한반복에 빠질 수 있음.
# 정수형: 비교 후 mid+1 / mid-1, 실수형: 비교 후 mid로 할당.
# => 실수형이므로 mid, mid+1 사이에 무수히 많은 경우의 수가 발생하기 때문임.

# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    N, L, W, H = map(int, input().split())
    largest = min(L, W, H)

    start, end = 0, largest

    # 🚨 diff = 1e-9(10의 -9승) 기준, while end - start >= diff: 로 이분탐색 진행 시 시간초과!
    # 대신 100번 반복하는방식을 사용해야함. 100번쯤 반복하면 오차가 1e-9보다 작아지게 됨.
    for _ in range(100):
        mid = (start + end) / 2
        cnt = (L//mid) * (W//mid) * (H//mid)

        if N <= cnt:
            start = mid
        else:
            end = mid
    
    print(f"{end:.10f}")


main()