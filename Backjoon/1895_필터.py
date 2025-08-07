# 구현
# 정렬
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/1895
# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    R, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(R)]
    T = int(input())

    cnt = 0

    # 필터의 크기는 3x3
    for r in range(R-2):
        for c in range(C-2):
            # 정렬 후 중간값 확인
            pixels = [arr[i][j] for i in range(r, r+3) for j in range(c, c+3)]
            pixels.sort()

            mid = pixels[4]

            if mid >= T:
                cnt += 1
    
    print(cnt)


main()