# 구현


# 문제: https://www.acmicpc.net/problem/3054
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    data = input().rstrip()
    frame = None

    arr = [["."] * (4 * len(data) + 1) for _ in range(3)]

    # 알파벳 순서가 3의 배수일때가 아니라, 주어진 문자열에서의 순서임.
    # ABCDEF이면 C, F를 웬디 프레임으로.
    for i, alp in enumerate(data):
        if i % 3 == 2:
            frame = "*"
        else:
            frame = "#"
        
        arr[0][i*4 + 2] = frame
        arr[1][i*4 + 1] = arr[1][i*4 + 3] = frame

        arr[2][i*4 + 4] = frame
        arr[2][i*4 + 2] = alp
        if arr[2][i*4] != "*":
            arr[2][i*4] = frame

    arr += [arr[1]] + [arr[0]]

    for line in arr:
        print(*line, sep="")


main()