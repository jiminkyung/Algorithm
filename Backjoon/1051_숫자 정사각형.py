# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/1051

# 완전탐색으로 풂. 최적화가 가능할까? 싶어서 생각해봤는데 어차피 완전탐색으로 풀어야할 듯.
# 메모리: 32412KB / 시간: 48ms
from sys import stdin


input = stdin.readline

def main():
    N, M = map(int, input().split())
    arr = [input().rstrip() for _ in range(N)]
    limit = min(N, M)  # 둘 중 더 작은값이 나올수있는 최대 정사각형 크기
    max_size = 1  # 네 꼭짓점이 일치하는 경우가 아예 없을경우, 숫자 하나로 크기 1의 정사각형을 만들 수 있음.

    # 일단 완전탐색으로 풀어보자.
    # 현재 위치 (x, y)로부터 size만큼 떨어진 위치(꼭짓점)를 체크한다.
    for size in range(1, limit):
        for x in range(N-size):  # size만큼 떨어진 위치가 좌표 크기를 넘어가는것을 방지
            for y in range(M-size):
                # 현재 좌표를 좌상단 꼭짓점으로 생각하고 우상단, 좌하단, 우하단 체크
                num = arr[x][y]
                for nx, ny in ((x, y+size), (x+size, y), (x+size, y+size)):
                    if arr[nx][ny] != num:
                        break
                else:
                    max_size = max(size+1, max_size)
    
    print(max_size ** 2)


main()