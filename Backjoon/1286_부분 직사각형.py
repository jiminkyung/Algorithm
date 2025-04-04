# 수학
# 조합론


# 문제: https://www.acmicpc.net/problem/1286

"""
0-based N*M 행렬 기준
(i, j)를 포함하는 연속 부분수열(직사각형)의 갯수
= (i+1) * (j+1) * (N-i) * (M-j)
= 차례대로 직사각형의 위, 왼쪽, 아래, 오른쪽이 될 수 있는 경우의 수다.
"""

# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    N, M = map(int, input().split())
    word = [input().rstrip() for _ in range(N)]

    field = []

    # 2x2 패턴이 되도록 저장
    for _ in range(2):
        for row in word:
            field.append(row + row)
    
    alphabet = [0] * 26

    # 2x2 패턴에 맞춰 N, M 크기 조정
    N *= 2
    M *= 2

    # (i, j)가 포함되는 직사각형의 갯수 구하기
    for i in range(N):
        for j in range(M):
            cnt = (i+1) * (j+1) * (N-i) * (M-j)
            alphabet[ord(field[i][j])-65] += cnt
    
    print(*alphabet, sep="\n")


main()