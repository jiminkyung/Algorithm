# 분할 정복

# 메모리: 31120KB / 시간: 52ms
# Programmers > 쿼드압축 후 개수 세기.py 참고

from sys import stdin


input = stdin.readline
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

ret = [0, 0]

def quadtree(row: int, col: int, size: int) -> None:
    """
    row, col: 행, 렬
    size: 검사할 색종이의 크기
    half: 색종이를 반으로 나눈 크기
    """
    color: int = paper[row][col]

    for i in range(row, row+size):
        for j in range(col, col+size):
            if paper[i][j] != color:
                half = size // 2
                # 좌상, 좌하, 우상, 우하 순서대로 재귀
                quadtree(row, col, half)
                quadtree(row+half, col, half)
                quadtree(row, col+half, half)
                quadtree(row+half, col+half, half)
                return
    ret[color] += 1  # 모든 색이 같다면 해당 색깔 결과값(0또는 1)에 1 추가

quadtree(0, 0, N)
print(f"{ret[0]}\n{ret[1]}")