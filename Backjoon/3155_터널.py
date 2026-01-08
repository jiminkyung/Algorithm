# 구현
# 그리디 알고리즘


# 문제: https://www.acmicpc.net/problem/3155

# 내가 풀고 왜 이렇게 풀었는지 까먹은 문제... 문제 자체는 간단한 그리디 문제임.
# 메모리: 46552KB / 시간: 112ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())

    # 그림을 보면, i번째 칸의 높이는 i+1번째 칸의 터널 높이에 따라 결정됨.
    # 시작점은 0, 도착점은 N 이어야 하는데... 주어진 좌표 갯수는 N개뿐임.
    # 따라서 마지막에 높이가 1 ~ -1 인 구간을 하나 더 추가해줘야 마지막 높이값까지 얻을 수 있음.
    # 어차피 i+1번째 칸의 터널 높이를 따져야하니 시작점의 높이(0번째)는 계산에 포함하지 않아도 됨.
    ceil = list(map(int, input().split())) + [1]
    floor = list(map(int, input().split())) + [-1]

    pos = 0  # 현재 높이
    ret = []
    for i in range(1, N+1):
        top, bottom = ceil[i]-1, floor[i]+1

        # 바닥 위치보다 낮다면 현재 위치를 바닥 높이로,
        if pos < bottom:
            pos = bottom
        # 천장 위치보다 높다면 현재 위치를 천장 높이로 지정해줌. (최대한 적게 움직이기)
        elif pos > top:
            pos = top
        
        ret.append(pos)

    print(*ret)


main()