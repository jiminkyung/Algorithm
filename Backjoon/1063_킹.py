# 구현
# 시뮬레이션


# 문제: https://www.acmicpc.net/problem/1063
# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    K, S, N = input().rstrip().split()
    directions = {"R": (0, 1), "L": (0, -1), "B": (1, 0), "T": (-1, 0),
                  "RT": (-1, 1), "LT": (-1, -1), "RB": (1, 1), "LB": (1, -1)}
    
    # 🚨배열의 행(위-아래) 기준이 아닌 좌표의 행(아래-위) 기준으로 주어지므로, 따로 처리해줘야함.
    kx, ky = 8-int(K[1]), ord(K[0])-65
    sx, sy = 8-int(S[1]), ord(S[0])-65

    for _ in range(int(N)):
        cmd = input().rstrip()
        dx, dy = directions[cmd]

        # 킹 먼저 이동 시도
        nx, ny = kx + dx, ky + dy

        # 새롭게 이동하려는 좌표가 범위 내에 위치한다면,
        if 0 <= nx < 8 and 0 <= ny < 8:
            # 만약 새로운 자리에 돌이 위치해있다면, 돌 이동이 가능한경우에만 킹과 돌 이동 진행
            if (sx, sy) == (nx, ny):
                nsx, nsy = sx + dx, sy + dy
                if not (0 <= nsx < 8 and 0 <= nsy < 8):
                    continue
                sx, sy = nsx, nsy
            kx, ky = nx, ny
    
    # 배열 기준으로 행 처리
    print(chr(ky + 65) + str(8 - kx))
    print(chr(sy + 65) + str(8 - sx))


main()