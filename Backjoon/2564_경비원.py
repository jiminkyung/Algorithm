# 구현
# 많은 조건 분기


# 문제: https://www.acmicpc.net/problem/2564

# 나중에 다시 풀어볼만한 문제
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    M, N = map(int, input().split())
    T = int(input())
    
    def calc(dir, x):
        """ (0, 0)부터 시계방향으로 이동했을때의 거리값 """
        # 1234 순서대로 북남서동
        if dir == 1:
            return x
        elif dir == 2:
            return M + N + (M-x)
        elif dir == 3:
            return 2*M + N + (N-x)
        else:
            return M + x
    
    coord = [tuple(map(int, input().split())) for _ in range(T)]
    curr = calc(*map(int, input().split()))  # 동근이의 현재 위치값
    ret = 0

    for dir, x in coord:
        dist = calc(dir, x)
        diff = abs(curr - dist)  # 동근이와 상점 사이의 거리(일직선상 기준 시계방향)
        # diff가 동근이 기준으로 시계방향인지, 반시계방향인지는 모름.
        # 뭐가 diff인지는 상관없이 시계/반시계 값 중 더 가까운 값으로 계산.
        ret += min(diff, 2 * (N + M) - diff)

    print(ret)


main()