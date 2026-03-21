# 수학
# 구현


# 문제: https://www.acmicpc.net/problem/3699
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        solve()


def solve():
    h, l = map(int, input().split())
    total = []

    for i in range(h):
        line = list(map(int, input().split()))
        for j in range(l):
            if line[j] != -1:
                total.append((line[j], i, j))
    
    total.sort()

    time = 0
    # 🚨 컨베이너 벨트는 층마다 존재.
    # 컨베이너 벨트는 이동 후 원래 자리로 돌아갈 필요 없음.
    # 엘리베이터는 1층으로 복귀해야함. (갖다줘야하니까)
    pos = [0] * h

    for num, i, j in total:
        time += i * 10 * 2  # 엘리베이터 이동 시간
        dist = 0

        # pos[i]: i층 컨테이너벨트의 현 위치
        # 시계방향, 반시계방향 이동 거리 계산 후 더 작은 값으로 선택.
        if pos[i] < j:
            dist = min(j - pos[i], pos[i] + (l - j))
        else:
            dist = min(pos[i] - j, (l - pos[i]) + j)
        
        # i층 컨베이너벨트 위치 갱신
        pos[i] = j
        time += dist * 5
    
    print(time)


main()