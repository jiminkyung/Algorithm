# 수학
# 구현
# 시뮬레이션


# 문제: https://www.acmicpc.net/problem/2980
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    N, L = map(int, input().split())
    time = dist = 0

    for _ in range(N):
        D, R, G = map(int, input().split())
        time += D - dist  # 기존 위치에서 신호등까지 온 거리 더해줌

        # 현재 시간을 해당 신호등의 사이클로 나눠줌
        # 나머지 시간 -> 신호등의 현재 사이클에 해당되는 시간
        curr = time % (R + G)
        if curr < R:  # 만약 현재 사이클의 시간이 빨간불에 해당되는 시간이라면 기다림
            time += (R - curr)
        
        dist = D  # 위치 갱신
    
    # 마지막 신호등에서 L까지의 거리 더해줌
    time += (L - D)
    print(time)


main()