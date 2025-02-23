# 문제집 - 0x1C강 - 플로이드 알고리즘


# 문제: https://www.acmicpc.net/problem/13141

# 애먹었던 문제다... 그리고 문제 설명이 모호한데, 그래프의 "모든 경로"가 타는것을 전제로 풀어야한다.
# start부터 A, B까지 불이 퍼져나갈때 '왜 start-A, start-B의 최장경로는 고려하지 않는걸까?'에 갇혀 무한 검색에 빠졌었다. (주석 참고)
# 다른 사람들의 풀이를 참고하고, 직접 풀어보니 생각보다 쉬웠던 문제. 나중에 다시 풀어볼만한 문제인듯.

# 참고1: https://magentino.tistory.com/455 (플로이드 워셜을 두번 수행하는것과 비슷)
# 참고2: https://rapun7el.tistory.com/244 (예쁜 풀이!)

# 메모리: 33432KB / 시간: 3788ms
from sys import stdin


input = stdin.readline
INF = float("inf")

N, M = map(int, input().split())
max_dis = [[-1] * N for _ in range(N)]
min_dis = [[INF] * N for _ in range(N)]

for _ in range(M):
    S, E, L = map(int, input().split())
    S -= 1
    E -= 1

    if max_dis[S][E] < L:
        max_dis[S][E] = max_dis[E][S] = L
    if min_dis[S][E] > L:
        min_dis[S][E] = min_dis[E][S] = L


for k in range(N):
    min_dis[k][k] = 0
    for i in range(N):
        for j in range(i+1, N):  # 양방향 간선이므로 절반까지만 계산해줌
            min_dis[i][j] = min_dis[j][i] = min(min_dis[i][k] + min_dis[k][j], min_dis[i][j])


ret = INF

for start in range(N):
    time = 0.0
    for i in range(N):
        for j in range(N):  # i+1부터 시작하도록 잡으면 자기 자신으로 돌아오는 간선을 계산하지 못함. ex) 3 3 4 : 3번노드에서 3번노드까지의 간선길이 4
            if max_dis[i][j] == -1:
                continue

            # curr_time = (i, j까지 최단거리 + i-j의 최장거리) / 2
            # i, j까지의 최장경로는 고려하지 않아도 됨.
            # 👉 i = j가 될 경우, 이전에 건너뛰었던 "최장경로가 타는 시간"도 자연스럽게 계산.
            curr_time = (min_dis[start][i] + min_dis[start][j] + max_dis[i][j]) / 2
            time = max(time, curr_time)  # start부터 시작해서 전체 간선이 타는 최장 시간
    
    ret = min(ret, time)  # 최장 시간 중 가장 최소가 되는 시간을 선택


print(f"{ret:.1f}")


# 참고2 버전 풀이
# 모두 더한 뒤 한꺼번에 / 2 를 해주니 깔끔함.
# 메모리: 35480KB / 시간: 3960ms
from sys import stdin


input = stdin.readline
INF = float("inf")

N, M = map(int, input().split())

graph = []
min_dis = [[INF] * N for _ in range(N)]

for _ in range(M):
    S, E, L = map(int, input().split())
    S -= 1
    E -= 1

    min_dis[S][E] = min_dis[E][S] = min(min_dis[S][E], L)
    graph.append((S, E, L))


for k in range(N):
    min_dis[k][k] = 0
    for i in range(N):
        for j in range(N):
            min_dis[i][j] = min(min_dis[i][k] + min_dis[k][j], min_dis[i][j])


ret = INF

for start in range(N):
    time = 0
    for S, E, L in graph:
        time = max((min_dis[start][S] + min_dis[start][E] + L) / 2, time)
    ret = min(time, ret)

print(ret)