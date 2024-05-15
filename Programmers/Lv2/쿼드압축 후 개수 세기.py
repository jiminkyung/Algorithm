"""
재귀함수를 사용하는 문제.

quad 함수를 통해 주어진 행, 열을 순회하며 체크한다.
만약 다른 값이 존재한다면 해당 블록을 좌상, 우상, 좌하, 우하로 나누어 다시 순회.
모두 같은 값이라면 해당 값의 개수를 1 증가시킨다.
- ret[0의개수, 1의개수] 이므로 블록이 모두 0이라면 ret[0] += 1, 1이라면 ret[1] += 1로 해결할 수 있다.
"""

def solution(arr: list) -> list:
    ret = [0, 0]

    def quad(row, col, size):
        default = arr[row][col]
        for r in range(row, row+size):
            for c in range(col, col+size):
                if arr[r][c] != default:
                    half = size // 2
                    quad(row, col, half)
                    quad(row, col + half, half)
                    quad(row + half, col, half)
                    quad(row + half, col + half, half)
                    return
        ret[default] += 1
    
    quad(0, 0, len(arr))
    return ret