# 수학
# 이분 탐색


# 문제: https://www.acmicpc.net/problem/3541

# 알고리즘 분류 보는 습관을 고쳐야겠다...
# 메모리: 32412KB / 시간: 48ms
from sys import stdin


input = stdin.readline

def main():
    n, m = map(int, input().split())


    def binary_search(u: int, d: int) -> int:
        # 🗝️ 최대한 적은 횟수로 올라가야 함.
        # 올라가는 횟수를 k번이라 치면, 내려가는 횟수는 (n - k)임.
        # 최소 k값 == 이번 엘리베이터에서의 답!
        start, end = 0, n
        ret = n

        while start <= end:
            mid = (start + end) // 2
            res = mid * u - (n - mid) * d
            
            if res <= 0:
                start = mid + 1
            else:
                ret = mid
                end = mid - 1
            
        return ret * u - (n - ret) * d
    

    min_floor = float("inf")

    for _ in range(m):
        u, d = map(int, input().split())
        min_floor = min(min_floor, binary_search(u, d))
    
    print(min_floor)


main()