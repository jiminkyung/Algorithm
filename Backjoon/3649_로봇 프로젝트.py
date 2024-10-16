# 문제집 - 대학생 기본반


# 문제: https://www.acmicpc.net/problem/3649
# 여러개의 테스트 케이스가 주어지지만, 몇개인지는 알려주지 않는다.
# 처음엔 set()로 풀었는데, 이분 탐색/투 포인터 문제였다.

# 메모리: 115168KB / 시간: 4504ms
from sys import stdin


input = stdin.readline

while True:
    try:
        x = int(input()) * 10000000
        n = int(input())

        lego = [int(input()) for _ in range(n)]
        lego.sort()

        left, right = 0, n-1

        r1 = r2 = 0
        while left < right:
            if lego[left] + lego[right] < x:
                left += 1
            elif lego[left] + lego[right] > x:
                right -= 1
            else:
                r1, r2 = lego[left], lego[right]
                break
        
        print(f"yes {r1} {r2}" if r1 != 0 else "danger")
    except:
        break