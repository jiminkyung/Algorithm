# 분할 정복

# 메모리: 31120KB / 시간: 40ms
# 2630번 색종이만들기 문제와 비슷함.

from sys import stdin


input = stdin.readline
N = int(input())
# 마지막에 join()을 사용할 예정이므로 형 변환없이 str값 그대로 리스트에 더해준다.
dots: list[str] = [input() for _ in range(N)]

ret = []

def quadtree(row: int, col: int, size: int) -> None:
    """
    만약 첫번째 값과 [i][j]의 값이 다르다면,
    여는괄호"("를 더해준 뒤 좌상, 우상, 좌하, 우하의 순서로 재귀호출한다.
    호출을 마치고 닫는괄호")"를 더해준다.

    모든 값이 동일하다면 그 값을 더해준다.
    """
    dot = dots[row][col]

    for i in range(row, row+size):
        for j in range(col, col+size):
            if dots[i][j] != dot:
                ret.append("(")
                half = size // 2
                quadtree(row, col, half)
                quadtree(row, col+half, half)
                quadtree(row+half, col, half)
                quadtree(row+half, col+half, half)
                ret.append(")")
                return
    ret.append(dot)

quadtree(0, 0, N)
print("".join(ret))