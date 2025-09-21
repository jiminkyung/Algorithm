# 문제집 - 0x1C강 - 플로이드 알고리즘


# 문제: https://www.acmicpc.net/problem/11562

# 더 빠른 풀이 (로직은 같음)
# 메모리: 32412KB / 시간: 1152ms
from sys import stdin


input = stdin.readline
INF = int(1e9)

def main():
    # 건설되어 있는 도로(양방향, 일반도로 u -> v)라면 0으로 설정.
    # 일반 도로에서 역방향, v -> u의 값은 1로 설정한다.
    # => 건설되지 않은 역방향 도로 v -> u가 최단거리에 포함되는 갯수 = 양방향 도로로 변경해야하는 도로의 갯수
    N, M = map(int, input().split())
    graph = [[INF if i != j else 0 for j in range(N)] for i in range(N)]

    for _ in range(M):
        u, v, b = map(int, input().split())
        graph[u-1][v-1] = 0

        if b == 1:
            graph[v-1][u-1] = 0
        else:
            graph[v-1][u-1] = 1

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    
    K = int(input())
    ret = []
    for _ in range(K):
        s, e = map(int, input().split())
        print(graph[s-1][e-1])
    

main()


# 메모리: 34456KB / 시간: 4928ms
from sys import stdin


input = stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
graph = [[INF] * (N+1) for _ in range(N+1)]

# 건설되어 있는 도로(양방향, 일반도로 u -> v)라면 0으로 설정.
# 일반 도로에서 역방향, v -> u의 값은 1로 설정한다.
# => 건설되지 않은 역방향 도로 v -> u가 최단거리에 포함되는 갯수 = 양방향 도로로 변경해야하는 도로의 갯수
for _ in range(M):
    u, v, b = map(int, input().split())
    
    graph[u][v] = 0
    graph[v][u] = 0

    if b == 0:
        graph[v][u] = 1


for k in range(1, N+1):
    graph[k][k] = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])


K = int(input())
for _ in range(K):
    s, e = map(int, input().split())
    print(graph[s][e])