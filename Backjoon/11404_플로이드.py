# 최단 경로

# 플로이드-워셜 알고리즘 문제
# 한 노드에서 모든 노드까지가 아닌, 모든 노드간의 최단거리를 구할 수 있는 알고리즘이다.
# 시작노드가 i, 도착노드가 j일때 노드 k를 거쳐가는 경우를 확인한다. dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])


# 메모리: 42140KB / 시간: 376ms
from sys import stdin


input = stdin.readline
INF = int(1e9)
n = int(input())
N = n + 1
m = int(input())

bus = []
for _ in range(m):
    bus.append(tuple(map(int, input().split())))

def floyd_warshall():
    dp = [[INF]*(N) for _ in range(N)]

    for i in range(1, N):  # 자기 자신으로 가는 비용은 0으로 설정한다.
        dp[i][i] = 0

    for u, v, w in bus:  # 시작-끝이 같은 노선이 여러 개 있을 수 있기 때문에 최소값인 노선으로 설정하도록 한다.
        dp[u][v] = min(dp[u][v], w)
    
    for k in range(1, N):  # 거치는 부분
        for i in range(1, N):  # 시작점
            for j in range(1, N):  # 끝점
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    return dp

ret = floyd_warshall()

for i in range(1, N):
    for j in range(1, N):
        if ret[i][j] == INF:
            ret[i][j] = 0
    print(*ret[i][1:])