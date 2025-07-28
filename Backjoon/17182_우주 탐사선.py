# 문제집 - 0x1C강 - 플로이드 알고리즘


# 문제: https://www.acmicpc.net/problem/17182

# 최소 신장 트리 문제인줄 알았으나 아님!
# 재방문이 가능하긴 하나, 비용이 발생하는 구조.

# 🗝️ 플로이드 워셜 수행 후 DP / DFS 를 사용해야 함.

# 1) DP + 비트마스킹 사용 풀이
# top-down 방식으로 수행하므로 메모이제이션 사용. 덕분에 실행시간이 DFS만 사용했을때보다 훨씬 빠름.
# 메모리: 32412KB / 시간: 44ms
from sys import stdin


input = stdin.readline
INF = int(1e9)

N, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 1. 플로이드-워셜로 두 행성간의 최단거리를 구해줌.
for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

# 2. DP로 최적의 경로를 구함
# dp[curr][visited] = 현재 행성 curr에서 시작해서, 아직 방문하지 않은 모든 행성을 탐사하는데 필요한 최소 시간
dp = [[-1] * (1 << N) for _ in range(N)]

def find(curr, visited):
    if visited == (1 << N) - 1:
        return 0

    if dp[curr][visited] != -1:
        return dp[curr][visited]
    
    dp[curr][visited] = INF

    for nxt in range(N):
        # 방문하지 않은 행성일경우
        if not (visited & (1 << nxt)):
            cost = graph[curr][nxt] + find(nxt, visited | (1 << nxt))
            dp[curr][visited] = min(dp[curr][visited], cost)
    return dp[curr][visited]


print(find(K, 1 << K))


# 2) DFS 사용 풀이
# 메모리: 32412KB / 시간: 3120ms
from sys import stdin


input = stdin.readline
INF = int(1e9)

N, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 1. 플로이드-워셜로 두 행성간의 최단거리를 구해줌.
for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

# 최소 신장 트리 문제인줄 알았으나 아님!
# 재방문이 가능하긴 하나, 비용이 발생하는 구조.

# 2. DFS 수행
visited = [False] * N
min_time = int(1e9)

# curr: 현재 위치한 행성, time: 현재까지의 총 시간
def dfs(cnt, curr, time):
    global min_time

    if cnt == N:
        min_time = min(time, min_time)
        return
    
    for i in range(N):
        if visited[i]:
            continue

        visited[i] = True
        dfs(cnt+1, i, time + graph[curr][i])
        visited[i] = False


dfs(0, K, 0)
print(min_time)