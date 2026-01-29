# 구현
# 정렬
# 시뮬레이션


# 문제: https://www.acmicpc.net/problem/3196

# 아래처럼 해시로 관리하면 편한 문제인듯.
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    K, N, M = map(int, input().split())

    # 선수마다 (다음으로 방문해야 할 체크포인트, 마지막 통과 시간, 통과한 체크포인트 수) 저장.
    # 🚨 마지막 체크포인트 찍고 다시 1번부터 시작 가능. cnt로 통과한 체크포인트 수를 따로 저장해줘야 편할듯.
    player = {i+1: {"nxt": 1, "time": -1, "cnt": 0} for i in range(N)}

    for i in range(M):
        X, Y = map(int, input().split())

        # 다음번에 방문해야 할 체크포인트가 맞을 경우
        if player[X]["nxt"] == Y:
            player[X]["nxt"] = Y % K + 1
            player[X]["time"] = i
            player[X]["cnt"] += 1
    
    # 1. 통과한 체크포인트가 많은 순서, 2. 체크포인트를 더 빨리 통과한 순서대로 정렬. (내림차순, 오름차순)
    ret = sorted(player.keys(), key=lambda x: (-player[x]["cnt"], player[x]["time"]))
    print(*ret)


main()